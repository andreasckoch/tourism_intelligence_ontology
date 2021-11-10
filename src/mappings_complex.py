from rdflib import XSD

def no_space(input):
    return input.strip().replace(' ', '_')

data_property_mapping = {
    'country_of_residence': 'LUGAR_RESIDENCIA',
    'tourists': 'VIAJEROS',
    'overnight_stays': 'PERNOCTACIONES',
    'establishments': 'ESTABLECIMIENTOS_ESTIMADOS',
    'parcels': 'PARCELAS',
    'places': 'PLAZAS_ESTIMADAS',
    'degree_of_occupied_parcels': 'GRADO_OCUPA_PARCELAS',
    'degree_of_occupied_parcels_on_weekends': 'GRADO_OCUPA_PARCELAS_FIN_SEMANA',
    'number_of_occupied_parcels': 'NUM_PARCELAS_OCUPADAS',
    'personel_employed': 'PERSONAL_EMPLEADO',
    'category': 'CATEGORIA',
    'country_of_origin': 'PAIS',
    'province': 'PROVINCIA',
    'degree_of_occupied_places': 'GRADO_OCUPA_PLAZAS',
    'degree_of_occupied_places_on_weekends': 'GRADO_OCUPA_PLAZAS_FIN_SEMANA',
    'apartments': 'APRTAMENTOS_ESTIMADOS',
    'degree_of_occupied_apartments': 'GRADO_OCUPA_APART',
    'degree_of_occupied_apartments_on_weekends': 'GRADO_OCUPA_APART_FIN_SEMANA',
    'average_duration_of_stay': 'ESTANCIA_MEDIA',
    'rooms': 'HABITACIONES_ESTIMADAS',
    'degree_of_occupied_hotel_rooms': 'GRADO_OCUPA_POR_HABITANTES',
    'degree_of_occupied_rural_rooms': 'GRADO_OCUPA_HABITACIONES',
}

xsd_type_mapping = {
    'country_of_residence': XSD.string,
    'tourists': XSD.integer,
    'overnight_stays': XSD.integer,
    'establishments': XSD.integer,
    'parcels': XSD.integer,
    'places': XSD.integer,
    'degree_of_occupied_parcels': XSD.float,
    'degree_of_occupied_parcels_on_weekends': XSD.float,
    'number_of_occupied_parcels': XSD.integer,
    'personel_employed': XSD.integer,
    'category': XSD.string,
    'country_of_origin': XSD.string,
    'province': XSD.string,
    'degree_of_occupied_places': XSD.float,
    'degree_of_occupied_places_on_weekends': XSD.float,
    'apartments': XSD.integer,
    'degree_of_occupied_apartments': XSD.float,
    'degree_of_occupied_apartments_on_weekends': XSD.float,
    'average_duration_of_stay': XSD.float,
    'rooms': XSD.integer,
    'degree_of_occupied_hotel_rooms': XSD.float,
    'degree_of_occupied_rural_rooms': XSD.float,
}

object_property_mapping = {
    'year': 'AÑO',
    'month': 'MES',
    'region': 'CCAA',
    'touristic_point': 'PUNTO_TURISTICO',
    'touristic_zone': 'ZONA_TURISTICA',
}

name_mapping = {
    'categoria': 'Category',
    'ccaa': 'Region',
    'pais': 'Country_Of_Origin',
    'provincia': 'Province',
    'punto_turistico': 'Touristic_Point',
    'zona_turistica': 'Touristic_Zone',
}

accom_type_mapping = {
    'eoac': 'Camping_Sites',
    'eoal': 'Hostels',
    'eoap': 'Touristic_Apartments',
    'eoh': 'Hotels',
    'eotr': 'Rural_Touristic_Apartments',
}

class_mapping = {
    'eoac': 'Camping_Sites_Statistics',
    'eoal': 'Hostels_Statistics',
    'eoap': 'Touristic_Apartments_Statistics',
    'eoh': 'Hotels_Statistics',
    'eotr': 'Rural_Touristic_Apartments_Statistics',
}
