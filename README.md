# Stable Diffusion Text2Img App
This web application leverages the Stable Diffusion deep learning model to generate images based on user-provided prompts.

The application is built using React for the frontend and FastAPI for the backend. The Stable Diffusion model is loaded and run on the server using PyTorch. The generated images are then sent back to the client as base64-encoded PNG files, which are displayed using the Image component provided by the Chakra UI library.

## Screenshot
![Keynote](https://github.com/Marckwin/text2imgreact/blob/main/dragon.jpg)

## Getting Started
To run the application locally, follow these steps:

Clone the repository:
git clone https://github.com/<username>/stable-diffusion-text2img.git

Install the required packages:
pip install -r requirements.txt
npm install

Start the server:
python app.py

In a separate terminal window, start the client:
npm start

Open your web browser and go to http://localhost:3000 to use the application.

## Usage
Enter a prompt in the input field and click the "Generate" button.
Wait for the model to generate the image (this may take a few seconds).
The generated image will be displayed on the page.




