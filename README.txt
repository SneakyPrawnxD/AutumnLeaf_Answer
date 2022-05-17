Autumn Leaf Assessment Answers: 

Within this folder you will find 7 different files. 

1. Dockerfile
2. Instrustions
3. Main2.py
4. question1_Answer.py
5. question2_Answer.py
6. README.txt
7. test_question.py

The original instructions for assessment can be found within the Instructions file. The instructions asked for 6 different tasks to be completed.

For these questions you require: 
- The preferred OS is Ubuntu
- Pyhton
- pip, pip pytest and pip requests
- Docker

Before assessing the files, please download the files and create a flder named App and place the files in that folder.

Question 1: Add 1 line of code to the function in question1.py to let the output print 4 and run.

	Answer: In the original code the variable "counter" was declared outside of the definition of the function. The definition was then not able to call on the variable. Declaring the variable within the definition resolves this problem. 
	
	How to test that this is true: 
	1. Open Terminal
	2. Navigate to the folder named App on terminal
	3. In terminal enter and run: python3 Q1_Answer.py
	
	The output will be 4, which is the requested answer.

Question 2: Use pytest to make the function in question2.py run.

	Answer: To test the logic with pytest for the script in Question2.py, the original has been renamed to test_Q2.py

	How to test using pytest: 
	1. Open Terminal
	2. Navigate to the folder named App on terminal
	3. In terminal enter and run: pytest test_Q2.py 

	This will return with with a fail, you can see in the test output that 4 does not equal 5. To fix this, a duplicate file was created and named test_Q2Answer.py, the parameter x has been changed from 3 to 4. 

	How to test the updated script: 
	1. Within the same terminal session enter and run: pytest test_Q2Answer.py 

	This will return with a Pass, as the logic x = 5 proves correct. 

Question 3: Write python script which will loop and hit a website during the loop and record total time of requests. 
	The script should get the number of iterations and site name from environment variables.
    	Hint: use requests library.

	Answer: A new script was created and named Main2.py. Within this script a loop has been created that visits a weblink and records the amount of time it took for the request returns. The website and amount of loops are determined by environment variables. The request time is recorded and printed, at the end the total request time is printed as well. 

	How to run the script:
	1. Open Terminal
	2. Navigate to the folder named App on terminal 
	3. In terminal enter and run: python3 Main2.py

	Once the script has ran the output will show each loop, the amount of time the request took and the URL that was visited. The last output will be the total time the requests took.

Question 4: Create a docker image of the python script where you input the environment variables for the script to use and then run it to display the total time.

	Answer: A Dockerfile has been created to run the script that was created in Question 3. The docker file determines the environment variables, which is used by the script. 

	Answer: How to deploy build and deploy the docker image: 
	1. Open Terminal
	2. Navigate to the folder named App in terminal
	4. Run the following command to build the docker image: Docker build  -t webtime .
	5. Once the image has completed bulding, run the image: Docker run webtime

	Once the Image is run the output will show each loop, the amount of time the request took and the URL that was visited. The last output will be the total time the requests took.
