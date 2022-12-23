import arcpy
import parsers
import wrapper

inst = wrapper.PocInstrumentation()
wrapper.PocInstrumentation.add_parser(parsers.TrivialParser())

@inst.fn_inst
def i_am_a_function(a: str, b: str = None) -> str:
    result: str = f"Hello, world! {a} {b}"
    return result

@inst.fn_inst
def do_first_set(primary_sde, secondary_sde, scratch_gdb) -> None:
    arcpy.MakeFeatureLayer_management(scratch_gdb, "fc")
    arcpy.SpatialJoin_analysis(primary_sde, scratch_gdb, "fc", secondary_sde)

@inst.fn_inst
def do_second_set(primary_sde, secondary_sde, scratch_gdb) -> None:
    arcpy.SelectLayersByLocation_management(primary_sde, scratch_gdb, "fc", "layer")
    arcpy.SpatialJoin_analysis(primary_sde, scratch_gdb, "fc", secondary_sde)

if __name__ == "__main__":
    print(f"- benchmarked zero time: {inst.zero_time}")
    primary_sde = None
    secondary_sde = None
    scratch_gdb = None
    do_first_set(primary_sde, secondary_sde, scratch_gdb)
    do_second_set(primary_sde, secondary_sde, scratch_gdb)
