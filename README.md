# bsurance Test

# Getting Started

First clone the repository from Github and switch to the new directory:
````
$ git https://github.com/adbrum/bsurance_upload.git
$ cd bsurance_upload
````

#### Activate the virtualenv for your project.
  
Install project dependencies:
```
$ pip install -r requirements.txt
```    

Then simply apply the migrations:
```
$ python manage.py migrate
```    

You can run the tests:
```
$ python manage.py test
```

You can now run the development server:
```
$ python manage.py runserver --insecure
```

- Use the **--insecure** option to force static files to be displayed with the staticfiles application, even if the DEBUG setting is False. This is for local development only, should never be used in production, and is only available if the staticfiles application is in your project's INSTALLED_APPS setting.

## Below are the answers for each topic.

1. Choose any python web framework you like and create a web which fulfills the following use cases:


   - Use case 1:

     As a user I want to upload and name an image.

     - [X] Scenario 1:

       Given image named "blue" do not exist
       When I access page with upload form
       And I set "blue" in name field
       And I click select button
       And I select a image from the system
       Then I see a confirmation message "blue image uploaded"
       And I can access the image in /img/blue url

     - [X] Scenario 2:

         Given image named "blue" do exist
         When I access page with upload form
         And I set "blue" in name field
         And I click select button
         And I select a image from the system
         Then I see a confirmation message "blue image changed"
         And I can access the new image in /img/blue url

    - Use case 2:

       As a user I want to access a named image.

         - [X] Scenario 1:

             Given image named "blue" do not exist
         blue    When I access page /image/blue
             Then I see a 404 page

         - [X] Scenario 2:

             Given image named "blue" do exist
             When I access page /image/blue
             Then I see the "blue" image with the text "blue image" on top

2. In the context of previous applications. Explain how would you improve the time load for the html pages that contained the uploaded images. Order the improvements from the first you would do to the last maximizing benefit/cost, please explain your ordering.

    ### Answer:
    One of the main actions to reduce the loading time of a web page is image formatting. Large images slow down web pages, which creates a less-than-optimal user experience. Optimizing images is the process of decreasing the file size, using a plugin or script, which, as far as you are concerned, speeds up page load times. Lossy and lossless compression are the two commonly used methods.

      - File format and the compression category it uses. By choosing the right combination of file format and compression category, you can reduce your image size up to 5 times.

      - Choosing the correct File Format, make sure you have chosen the best file category. There are several categories of files you can use for better loading, PNG, JPEG or GIF.

3. Imagine we want to use a 3th party library in order to re-size images during the upload. Explain how would you keep dependencies in the different environments, e.g. QA vs production (Choose for the explanation any OS and tools you prefer). 
    ### Answer:
    ### Development
    Have an isolated environment where you can code without worrying about the rest of the team. That's the premise of the development environment.
    It's simple to build an isolated environment on our machines, isolated even from our OS. We can code, test, make mistakes and fix, without directly affecting other team members.

    ### Testing
    When you have a test team on your project, there's nothing better than setting up a server where you can test the latest changes made to your application.
    Although unit and acceptance tests are largely performed in a development environment, when the project gets huge, running all the project tests with each new feature developed can be time-consuming. In this case it is interesting that you build a continuous integration server.

    ### staging
    The role of the staging environment is to be as close to reality as possible, that is, it must be a perfect replica of the production environment. In the case of web development, you must use the same web service, the same database, the same modules and plugins. This will ensure a much “smooth” deployment to the production environment.

    ### Production
    And finaAnd finally, the production environment. It is in this environment that the application comes to life and faces the harsh reality of the world.

4. Imagine we want to count how many people see a picture without using an external service e.g Google Analytics. Explain how would you do this. Take into account two scenarios, first a low traffic scenario and then a high traffic scenario.
    ### Answer:
    - Low traffic - An access counter in the patina where the images are.
    ````
    def index(request):
        ...

        # Number of visits to this view, as counted in the session variable.
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1

        context = {
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_visits': num_visits,
        }

        # Render the HTML template index.html with the data in the context variable.
        return render(request, 'index.html', context=context)
    ````

    - High traffic using Redis as a Cache - Cache is a resource that makes it possible to access information more quickly. Basically, it is a way to store certain information that is consumed more frequently so that it is available in the shortest possible time.
