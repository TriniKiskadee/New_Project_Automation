import os
import sys
import tkinter as tk
from tkinter import simpledialog
from selenium import webdriver
import subprocess

def newProjectDirectory(projectName):
    # My default project directory
    filePath = 'C:\\Users\\Renaud\\Desktop\\Python Projects'

    # Navigate to default project directory
    os.chdir(filePath)

    # Create folder for new project
    if (os.path.exists(filePath + "\\" + projectName) == False):
        os.mkdir(projectName)
        os.chdir(projectName)
        open("README.md", "+w")
        os.startfile(filePath + "\\" + projectName)

    else:
        #print("File Already exists")
        os.chdir(projectName)
        open("README.md", "+w")
        os.startfile(filePath + "\\" + projectName)

    if (os.path.exists(filePath + "\\" + projectName + "\\.git") == False):
        os.system('cmd /c "git init"')

def webNavigation(projectName):
    browser = webdriver.Firefox()
    url = 'https://github.com/login'
    username = ''
    password = ''

    browser.get(url)

    # enter login info to browser
    python_button = browser.find_element_by_xpath('//*[@id="login_field"]')
    python_button.send_keys(username)
    python_button = browser.find_element_by_xpath('//*[@id="password"] ')
    python_button.send_keys(password)
    python_button = browser.find_element_by_xpath('/html/body/div[3]/main/div/form/div[3]/input[8]')
    python_button.click()

    # create new repo
    python_button = browser.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div/div/h2/a')
    python_button.click()
    python_button = browser.find_element_by_xpath('//*[@id="repository_name"]')
    python_button.send_keys(projectName)
    python_button = browser.find_element_by_css_selector('button.btn.btn-primary.first-in-line')
    python_button.submit()

    browser.close()

# def dialogBox():
#     ROOT = tk.Tk()
#     ROOT.withdraw()

if __name__ == '__main__':
    # Dialog box, input used to name project folder
    ROOT = tk.Tk()
    ROOT.withdraw()
    newProject = simpledialog.askstring(title = "New Project", prompt = "Project Name: ")
    newProjectDirectory(newProject)
    webNavigation(newProject)
    subprocess.call(['C:\\Users\\Renaud\\Desktop\\Python Projects\\New_Project_Automation\\create.bat', newProject])
