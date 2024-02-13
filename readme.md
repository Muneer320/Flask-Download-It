# Download-It

Download-It is a Flask-based web application designed to facilitate the easy and quick download of videos from the internet. Users can simply enter the URL of the video they want to download, and the application will handle the rest, providing the video for download in little to no time.

## Dependencies

The project relies on the following dependencies, which are listed in the `requirements.txt` file:

- click==7.1.2
- Flask==1.1.2
- gunicorn==20.1.0
- itsdangerous==1.1.0
- Jinja2==2.11.3
- MarkupSafe==1.1.1
- Werkzeug==1.0.1
- youtube-dl==2021.4.26

## How to Run

To run the Download-It web application, follow these steps:

1. Ensure you have Python installed on your system.

2. Clone the repository to your local machine:
   ```
   git clone https://github.com/Muneer320/Flask-Download-It.git
   ```

3. Navigate to the project directory:
   ```
   cd Download-It
   ```

4. Install the dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

5. Run the Flask application:
   ```
   flask run
   ```

6. Access the application by navigating to `http://127.0.0.1:5000` in your web browser.

## How to Use

1. Once the application is running, you will be presented with a simple web interface.

2. Enter the URL of the video you want to download into the provided input field.

3. Click the "Download" button.

4. The application will begin processing the request and initiate the download of the video.

## Additional Information

For more information and help on how to use the Download-It application, refer to the "How-To" page within the application interface.