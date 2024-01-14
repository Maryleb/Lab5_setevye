from app import app
from flask import render_template, request
import constants
import numpy as np

@app.route('/', methods=['GET'])
def index():
    operation_id = []
    # список из выбранных пользователем дисциплин
    operations_select = []
    numbers = []
    numbers_list = []
    numbers_array = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    operation_id = request.values.getlist('operation[]')
    operations_select = [constants.operations[int(i)] for i in operation_id]
    if request.values.get('matrix_size') != None:
        for i in range(0, int(request.values.get('matrix_size'))):
            for j in range(0, int(request.values.get('matrix_size'))):
                index = j+int(request.values.get('matrix_size'))*i
                val = str(index)
                numbers.append((request.values.get(val)))
            numbers_list.append(numbers)
            numbers = []
        numbers_array = np.array(numbers_list)
        numbers_array = np.float64(numbers_array)
        print(numbers_array)

    html = render_template(
        'index.html',
         matrix_size = request.values.get('matrix_size'),
         operation_list=constants.operations,
         operations_select=operations_select,
         numbers_list = numbers_list,
         np = np,
         len = len,
         matrix = numbers_array

    )
    return html
