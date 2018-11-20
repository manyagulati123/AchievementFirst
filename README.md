# Instructions to run the script
1. If python is not installed on your machine then you can download it from https://www.python.org/downloads/
2. Clone this repository using following command in your terminal or command prompt
    ```
    git clone https://github.com/manyagulati123/AchievementFirst.git
    ```
3. Open the terminal or command prompt inside folder of this repository.
4. Run
    ```
    python main.py
    ```
5. This will return the list of all public repositories in my user account `manyagulati123`

# Customization
- If you want to get results of repositories from different github accounts, you can change line number 25 as follows:
    ```
    getRepos("https://api.github.com/users/<username_of_desired_account>/repos?", results)
    ```
- Currently the script will only be able to make 60 requests per hour, but can be increased to 5000 requests per hour by authenticating yourself.
  - To do so, change line number 5 to:
      ```
      response = requests.get(url + '&per_page=100', auth=(<your_github_email_id>, <your_github_password>)
      ```
