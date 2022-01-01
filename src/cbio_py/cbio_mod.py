from bravado.client import SwaggerClient as bravado_client

# This is the initialization of many of the data sources that we will need
cbioportal = bravado_client.from_url('https://www.cbioportal.org/api/api-docs', 
    config={"validate_requests":False,"validate_responses":False,"validate_swagger_spec": False,})

#Fetch all of the studies
def getAllStudies():
    studies = cbioportal.Studies.getAllStudiesUsingGET().result()
    return studies

def getAllCancerTypes():
    cancerTypes = cbioportal.Cancer_Types.getAllCancerTypesUsingGET().result()
    return cancerTypes

def getCancerByID(cancerTypeId):
    cancerType = cbioportal.Cancer_Types.getCancerTypeUsingGET(cancerTypeId=cancerTypeId).result()
    return cancerType

def getAllClinicalAttributes():
    clinicalAttributes = cbioportal.Clinical_Attributes.getAllClinicalAttributesUsingGET().result()
    return clinicalAttributes

def getClinicalAttributesByStudyId(studyId):
    clinicalAttributes = cbioportal.Clinical_Attributes.getAllClinicalAttributesInStudyUsingGET(studyId=studyId).result()
    return clinicalAttributes

def getClinicalAttributeInStudy(studyId, clinicalAttributeId):
    clinicalAttributes = cbioportal.Clinical_Attributes.getClinicalAttributeInStudyUsingGET(clinicalAttributeId=clinicalAttributeId,studyId=studyId).result()
    return clinicalAttributes

def getAllClinicalDataInStudy(studyId):
    clinicalData = cbioportal.Clinical_Data.getAllClinicalDataInStudyUsingGET(studyId=studyId).result()
    return clinicalData

def getAllClinicalDataOfPatientInStudy(studyId, patientId):
    clinicalData = cbioportal.Clinical_Data.getAllClinicalDataOfPatientInStudyUsingGET(studyId=studyId,patientId=patientId).result()
    return clinicalData

def getAllClinicalDataOfSampleInStudy(studyId, sampleId):
    clinicalData = cbioportal.Clinical_Data.getAllClinicalDataOfSampleInStudyUsingGET(studyId=studyId,sampleId=sampleId).result()
    return clinicalData

