#CODEXO - A FACIAL RECOGNITION ATTENDANCE SYSTEM

Overview
This project is a Face Recognition Attendance System using OpenCV and the face_recognition library. The system captures video from a webcam, recognizes known faces, and logs the attendance with the current time in a CSV file.

#Features
Real-time face recognition using webcam
Attendance logging with date and time
Stores attendance data in a CSV file

#Requirements
1. Python 3.x
2. OpenCV
3. face_recognition
4. numpy

#INSTALLATION
1. Clone the repository:
git clone https://github.com/aryan-91/codexo.git
cd face-recognition-attendance-system
3. Install the required packages:
pip install opencv-python
pip install face_recognition
pip install numpy
4. Place your images of known faces in the project directory and update the paths in the script accordingly.
   
#Usage
1. Run the script:
2. python attendance_system.py
3. The system will start capturing video from your webcam. When it recognizes a face, it will log the name and current time into a CSV file named with the current date (e.g., 2023-06-10.csv).

To stop the program, press the q key.

#Configuration
Adding Known Faces: Place images of known faces in the project directory and update the paths in the script.

#Contributing
1. Fork the repository.
2. Create a new branch: git checkout -b feature-branch-name
3. Make your changes and commit them: git commit -m 'Add some feature'
4. Push to the branch: git push origin feature-branch-name
5. Submit a pull request.

#Acknowledgements
This project uses the face_recognition library by Adam Geitgey.

#Contact
Created by ARYAN PANDEY - feel free to contact me!

