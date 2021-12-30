from bravado.client import SwaggerClient as bravado_client

# This is the initialization of many of the data sources that we will need
cbioportal = bravado_client.from_url('https://www.cbioportal.org/api/api-docs', 
    config={"validate_requests":False,"validate_responses":False,"validate_swagger_spec": False,})

#Fetch all of the studies
def getALLStudies():
    studies = cbioportal.Studies.getAllStudiesUsingGET().result()
    return studies

def getALLCancerTypes():
    cancerTypes = cbioportal.Cancer_Types.getAllCancerTypesUsingGET().result()
    return cancerTypes

def getCancerByID(id):
    cancerType = cbioportal.Cancer_Types.getCancerTypeUsingGET(cancerTypeId=id).result()
    return cancerType

def getALLClinicalAttributes():
    clinicalAttributes = cbioportal.Clinical_Attributes.getAllClinicalAttributesUsingGET().result()
    return clinicalAttributes

def getClinicalAttributesByStudyId(id):
    clinicalAttributes = cbioportal.Clinical_Attributes.getAllClinicalAttributesInStudyUsingGET(studyId=id).result()
    return clinicalAttributes
