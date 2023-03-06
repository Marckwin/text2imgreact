# Import necessary modules and classes
from auth_token import auth_token
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline
from io import BytesIO
import base64 

# Create a new FastAPI app
app = FastAPI()

# Add a CORS middleware to allow cross-origin resource sharing
app.add_middleware(
    CORSMiddleware, 
    allow_credentials=True, 
    allow_origins=["*"], 
    allow_methods=["*"], 
    allow_headers=["*"]
)

# Set the device to use for processing (GPU if available)
device = "cuda"

# Set the ID of the pre-trained model to use
model_id = "CompVis/stable-diffusion-v1-4"

# Load the pre-trained model as a StableDiffusionPipeline instance
pipe = StableDiffusionPipeline.from_pretrained(
    model_id, 
    revision="fp16",  # Use a specific revision of the model
    torch_dtype=torch.float16,  # Use half-precision floating point for faster processing
    use_auth_token=auth_token  # Pass an authentication token if necessary
)

# Move the model to the processing device
pipe.to(device)

# Define an endpoint for generating an image based on a prompt
@app.get("/")
def generate(prompt: str): 
    # Use automatic mixed precision to speed up processing
    with autocast(device): 
        # Generate an image using the pre-trained model and the given prompt
        image = pipe(prompt, guidance_scale=8.5).images[0]

    # Save the generated image as a PNG file
    image.save("testimage.png")

    # Convert the image to a base64-encoded string for easy transmission
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    imgstr = base64.b64encode(buffer.getvalue())

    # Return the base64-encoded image as a response to the client
    return Response(content=imgstr, media_type="image/png")
