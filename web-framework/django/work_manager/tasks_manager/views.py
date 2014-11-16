# coding: utf-8

from django.shortcuts import render_to_response


def index(request):
    my_var = '<Hello Japan!>'
    years_old = 15
    array_city_capitalize = ['Tokyo', 'Nagoya', 'Kyoto', 'Fukuoka']

    return render_to_response('jp/index.html',
                              {'my_var': my_var,
                               'years': years_old,
                               'cities': array_city_capitalize})
