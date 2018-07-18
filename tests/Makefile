SHELL := /bin/bash
OUTPUT_DIR=/tmp

unit_test:

function_test:
	pytest ./function

cli_test_physio:
	extractCMRRPhysio ./data/test.dcm  ${OUTPUT_DIR}
	#diff -u ${OUTPUT_DIR}/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_Info.log ./data/matlab_results/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_Info.log
	diff -u ${OUTPUT_DIR}/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_PULS.log ./data/matlab_results/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_PULS.log
	diff ${OUTPUT_DIR}/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_RESP.log ./data/matlab_results/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_RESP.log

	# rm ${OUTPUT_DIR}/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_Info.log
	# rm ${OUTPUT_DIR}/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_PULS.log
	# rm ${OUTPUT_DIR}/Physio_20171130_122138_c71e64f9-f493-4ca9-8e92-473f5e0616cc_RESP.log

cli_test_non-physio:
	extract_cmrr_physio ./data/test.dcm  ${OUTPUT_DIR}
	
singularity_test:
