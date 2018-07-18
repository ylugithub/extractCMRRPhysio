import os
import filecmp
import tempfile
import pydicom
import pytest
from extractCMRRPhysio.unwrapper import Unwrapper

@pytest.fixture
def tempdir():
    return tempfile.gettempdir()


#data path
@pytest.fixture
def data_path():
    file_path = os.path.dirname(os.path.realpath(__file__))
    file_path_split = file_path.split(os.sep)
    data_path = os.path.join(os.sep.join(file_path_split[0:-1]),'data')
    return data_path

#physio dicom    
@pytest.fixture
def full_physio_filename(data_path):
    full_physio_filename = os.path.join(data_path,'test.dcm')
    return full_physio_filename

#non-physio dicom
def test_Unwrapper_physio_data(full_physio_filename,tempdir,data_path):
    dicom_filename = full_physio_filename
    output_path = tempdir

    #apply
    unwrapper = Unwrapper(dicom_filename, output_path)
    full_log_filenames = unwrapper.apply()

    #matlab results path
    matlab_result_path = os.path.join(data_path,'matlab_results')
    
    #matlab results
    print(os.path.join(matlab_result_path,'Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_Info.log'))
    print(os.path.join(output_path,'Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_Info.log'))
    assert filecmp.cmp(os.path.join(matlab_result_path,'Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_Info.log'), 
                        os.path.join(output_path,'Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_Info.log') )

    # assert filecmp.cmp(os.path.join(matlab_result_path,'Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_PULS.log'), 
    #                    os.path.join(output_path,'Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_Info.log'))

    # assert filecmp.cmp(os.path.join(matlab_result_path,'Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_RESP.log'),
    #                    os.path.join(output_path,'Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_RESP.log'))

    

# @pytest.fixture
# def some_data():
#     return 42

# def test_some_data(some_data):
#      assert some_data==42

# diff ${OUTPUT_DIR}/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_Info.log ./data/matlab_results/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_Info.log
# 	diff ${OUTPUT_DIR}/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_PULS.log ./data/matlab_results/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_PULS.log
# 	diff ${OUTPUT_DIR}/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_RESP.log ./data/matlab_results/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_RESP.log


#'D:\OneDrive - The University of Western Ontario\projects\convert_CMRR_C2B_MB_from_matlab_to_python\extractCMRRPhysio\tests\data\matlab_results'
