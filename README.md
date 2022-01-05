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

A quick note about the return data types - this API, by default, return the data in a list of dictionaries. This is because the data that is natively return by the cbio curl API is in a list of custom classes such as `Study`, `Case`, `Sample`, etc. This is a bit cumbersome to work with and may not be the most efficient way to work with the data if you're using it for data analysis. 

If you would like for the data to be returned in the native format - all of the functions should support a `return_type` parameter that can be set to `native` to return the data in the native format.

### Studies

`getAllStudies(return_type = 'dict')` - this returns a list of all available studies.

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

### Gene Panels
`getAllGenePanels(return_type = 'dict')` - this returns a list of all available gene panels.

`getSpecificGenePanel(genePanelId, return_type = 'dict')` - this returns a list of gene panels with the given gene panel id.

### Genes 

`getAllGenes(return_type = 'dict')` - this returns a list of all available genes.

`getAliasForGene(geneId, return_type = 'dict')` - this returns a list of gene aliases for the given gene id.

`getGene(geneId, return_type = 'dict')` - this returns a list of genes with the given gene id.

### Molecular Profiles

`getAllMolecularProfiles(return_type = 'dict')` - this returns a list of all available molecular profiles.

`getMolecularProfile(molecularProfileId, return_type = 'dict')` - this returns a list of molecular profiles with the given molecular profile id.

`getMolecularProfileInStudy(studyId, molecularProfileId, return_type = 'dict')` - this returns a list of molecular profiles for the given study id and molecular profile id.

`getMutationsInMolecularProfile(molecularProfileId, sampleListId, projection='DETAILED', return_type = 'dict', append='yes')` - this returns a list of mutations for the given molecular profile id and sample list id. The `projection` parameter can be used to return more detailed information about the mutation. The `append` parameter implies that you would like to get ALL of the mutations for the given molecular profile id and sample list id - if you wish to get a customer molecular profile you will need to set the append parameter to 'no' and then set the molecular profile id and sample list id with the appropriate values in the fuction call. 

### Patients

`getAllPatients(return_type = 'dict')` - this returns a list of all available patients.

`getAllPatientsInStudy(studyId, return_type = 'dict')` - this returns a list of patients for the given study id.

`getPatientInStudy(studyId, patientId, return_type = 'dict')` - this returns a list of patients for the given study id and patient id.

### Samples

`getAllSamplesList(return_type = 'dict')` - this returns a list of all available samples.

`getSpecificSampleList(sampleListId, return_type = 'dict')` - this returns a list of samples with the given sample list id.

`getSampleListInStudy(studyId, sampleListId, return_type = 'dict')` - this returns a list of samples for the given study id and sample list id.

`getAllSamplesInStudy(studyId, return_type = 'dict')` - this returns a list of samples for the given study id.

`getAllSamplesOfPatientInStudy(studyId, patientId, return_type = 'dict')` - this returns a list of samples for the given study id and patient id.

`getSampleInStudy(studyId, sampleId, return_type = 'dict')` - this returns a list of samples for the given study id and sample id.

`getSamplesByKeyword(keyword, return_type = 'dict')` - this returns a list of samples for the given keyword.

## Potential Issues / Future Development

The `Treatement` api endpoint is not configured. I will hopefully be able to update the api to include this functionality in the future.

POST endpoints are not included in the api. All of the requests are GET requests.

