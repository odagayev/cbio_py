# cbio_py - a Python wrapper for the cbioportal Cancer API

This is a python package for accessing the [Cancer Genomics Portal](https://www.cbioportal.org/) [API](https://www.cbioportal.org/api-docs). The purpose of this package is to provide a simple wrapper for the API and return data in a format that is easy to work with.

## Quickstart

The module is available as a [pip package](https://pypi.org/project/cbio_py/) and can be installed with:
`pip install cbio_py`.

Then run the following command to get the list of available studies:
```
from cbio_py import cbio_mod as cb
cb.get_studies()
```

## Available Functions

The data retrieval functions are broken up over several key data types. The following sections provide a list of the available functions for each data type.

### Studies

`getAllStudies()` - this returns a list of all available studies.
`getSpecificStudy(studyId, return_type = 'dict')` - this returns a list of studies with the given study id.
`getStudyTags(studyId,return_type = 'dict')` - this returns a list of study tags given a study id.

### Cancers 

`getAllCancerTypes(return_type = 'dict')` - this returns a list of all available cancer types.
`getCancerByID(cancerTypeId, return_type = 'dict')` - this returns a list of cancer types with the given `cancertypeid`.

### Clinical Attributes
`getAllClinicalAttributes(return_type = 'dict')` - this returns a list of all available clinical attributes.
`getClinicalAttributesByStudyId(studyId, return_type = 'dict')` - this returns a list of clinical attributes for the given study id.
`getClinicalAttributeInStudy(studyId, clinicalAttributeId, return_type = 'dict')` - this returns a list of clinical attributes for the given study id and clinical attribute id.

### Clinical Data
`getAllClinicalDataInStudy(studyId, return_type = 'dict'):` - this returns a list of clinical data for the given study id.
`getAllClinicalDataOfPatientInStudy(studyId, patientId, return_type = 'dict')` - this returns a list of clinical data for the given study id and patient id.
` getAllClinicalDataOfSampleInStudy(studyId, sampleId, return_type = 'dict')` - this returns a list of clinical data for the given study id and sample id.

### Copy Number Segments
`getCopyNumberSegmentsInSampleInStudy(studyId, sampleId, return_type = 'dict')` - this returns a list of copy number segments for the given study id and sample id.

## Potential Issues