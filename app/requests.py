from urllib import request, parse
import json
from .models import Food

base_url = None
x_app_id = None
x_app_key = None
r = None

def configure_nutrients_request(app):
    global base_url, x_app_id, x_app_key,r
    x_app_id = app.config['X_APP_ID']
    x_app_key = app.config['X_APP_KEY']
    base_url = app.config['BASE_URL']

def get_details(query):
    '''Get details of the food from the passed query.
    '''

    # user_query = {"query": query }

    # headers = {'content-type': 'application/json', 'x-app-id':x_app_id,'x-app-key': x_app_key}

    # r = requests.post(base_url, headers=headers, data=user_query)

    req = request.Request(base_url, method="POST")
    req.add_header('Content-Type', 'application/json')
    req.add_header('x-app-id', x_app_id)
    req.add_header('x-app-key', x_app_key)
    data= {
        "query": query
    }
    data = json.dumps(data)
    data = data.encode()

    with request.urlopen(req, data=data) as url:
        get_nutrients_data = url.read()
        get_nutrients_response = json.loads(get_nutrients_data)./

        details_results = None

        if get_nutrients_response['foods']:
            details_results_list = get_nutrients_response['foods']
            details_results = process_results(details_results_list)
            
    return details_results


def process_results(results_list):

    results = []

    for result in results_list:
        food_name = result.get('food_name')
        brand_name = result.get('brand_name') 
        serving_qty = result.get('serving_qty') 
        serving_unit = result.get('serving_unit')
        serving_weight_grams = result.get('serving_weight_grams')
        nf_calories = result.get('nf_calories')
        nf_total_fat = result.get('nf_total_fat')
        nf_saturated_fat = result.get('nf_saturated_fat')
        nf_cholesterol = result.get('nf_cholesterol')
        nf_sodium = result.get('nf_sodium')
        nf_total_carbohydrates = result.get('nf_total_carbohydrates')
        nf_dietary_fiber = result.get('nf_dietary_fiber')
        nf_sugars = result.get('nf_sugars')
        nf_proteins = result.get('nf_proteins')
        nf_potassium = result.get('nf_potassium')
        photo = result.get('photo')
        meal_type = result.get('meal_type')

        food_obj = Food(food_name, brand_name, serving_qty, serving_unit, serving_weight_grams, nf_calories, nf_total_fat, nf_saturated_fat, nf_cholesterol, nf_sodium, nf_total_carbohydrates, nf_dietary_fiber, nf_sugars, nf_proteins, nf_potassium, photo, meal_type)

        results.append(food_obj)

    return results