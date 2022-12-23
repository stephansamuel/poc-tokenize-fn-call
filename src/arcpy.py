from helpers import sink, wait_long, wait_short, wait_micro

class da:

    class Editor:

        def __init__(self, workspace):
            wait_micro()
            sink(workspace)

def UpdateCursor(fc):
    '''
    Update a cursor.
    '''
    sink(fc)

def SpatialJoin_analysis(*args, **kwargs):
    '''
    Perform a spatil join between two feature classes.
    '''

    '''
    target_features,
    join_features,
    output_feature_class,
    join_operation=None,
    keep_all_target_features=True,
    field_map="",
    match_option="",
    search_radius=1,
    distance_field_name=None
    '''

    wait_long()
    sink(args)
    sink(kwargs)

def MakeFeatureLayer_management(*args, **kwargs):
    '''
    Create a new feature class.
    '''
    wait_short()
    sink(args)
    sink(kwargs)

def SelectLayersByLocation_management(*args, **kwargs):
    '''
    Select layers using a location as a criterion.
    '''
    wait_long()
    sink(args)
    sink(kwargs)

def MakeFeatureLayer_management(*args, **kwargs):
    '''
    Create a new feature class layer.
    '''
    wait_short()
    sink(args)
    sink(kwargs)

