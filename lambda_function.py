import os


def generate_sitemap():
    """
    This function uses the third party library `https://github.com/c4software/python-sitemap`
    to generate the sitemap in the project root. This uses the configuration from `config.json`.
    Visit the link to find more docs about the config file.
    """

    os.system("python libraries/python-sitemap/main.py --config config.json")
    print("Sitemap generated")


def lambda_handler(event, context):
    """
    This is the main function called in AWS lambda. This calls the other
    child functions to get the job done. The event and context are given by lambda.
    """

    generate_sitemap()


if __name__ == "__main__":
    lambda_handler(None, {})
