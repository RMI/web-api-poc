description = """
RMI's Web API Proof of Concept allows you deploy a simple REST API locally.

The API has a "Hello World" root page, as well as a health check at /health. 

It is designed to read in the mtcars dataset, currently stored as a csv locally.
With this csv in the src/data folder, the app will read the csv and allow it to
be accessed via the api/dataset endpoint or specific items in the mtcars dataset are 
avaialble at api/'model_name'

"""
