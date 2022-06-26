# Select_Star
#Prefix_Assignment Using DRF

#install virtualenv

python3 -m venv env
#activate virtual env

source env/bin/activate
#first install django and drf

pip install django
pip install djangorestframework
after successfull install run server
#call the post method api endpoint:

http://127.0.0.1:8000/prefix_data

JSON Payload example
{ "data_li":[ "bottle_deposit_amt", "bottle_deposit_amt_usd", "bottle_redemption_amt", "bottle_redemption_amt_usd", "bottle_water_tax_amt", "bottle_water_tax_amt_usd"]}

Output:

##{ "bottle_": [ "bottle_deposit_amt", "bottle_deposit_amt_usd", "bottle_redemption_amt", "bottle_redemption_amt_usd", "bottle_water_tax_amt", "bottle_water_tax_amt_usd" ]}

###Validation ERROR

1.List cannot be empty.

e.g: {data_li: []}

2.Type of object is not list

e.g:{data_li={}}

3.Others edge_case
