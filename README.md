



# Browsable API in Django REST

To enable this feature, we should specify text/html for the Content-Type key in the request header. It helps us to use web browsers to surf through the API and can make different HTTP requests.

The HTTPie command to accept text/html as follows:

http -v :8000/robot/ “Accept:text/html”



## Steps


- RobotCategory (Robot Categories)

- Manufacturer  (Manufacturer Details)

- Robot (Robot Details)



The RobotCategory model requires:

- Robot category name
- The Manufacturer model requires:


Manufacturer name

- The Robot model requires:


Robot name

- A foreign key to the RobotCategory model
- A foreign key to the Manufacturer model
- Currency
- Price
- Manufacturing date





