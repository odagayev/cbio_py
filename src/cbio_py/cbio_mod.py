from bravado.client import SwaggerClient as bravado_client

# This is the initialization of many of the data sources that we will need
cbioportal = bravado_client.from_url('https://www.cbioportal.org/api/api-docs', 
    config={"validate_requests":False,"validate_responses":False,"validate_swagger_spec": False,})

#Fetch all of the studies
def getAllStudies(return_type = 'dict'): #I assume the end user will prefer a dictionary object
    studies = cbioportal.Studies.getAllStudiesUsingGET().result()
    if return_type == 'dict':
        studies_list = []
        for study in studies:
            study_dict = {}
            for att in dir(study): #this code converts the cancer object into a more dictionary list
                study_dict[att] = getattr(study, att)
            studies_list.append(study_dict)
        return studies_list
    elif(return_type == 'native'):
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

def getCopyNumberSegmentsInSampleInStudy(studyId, sampleId):
    copyNumberSegments = cbioportal.Copy_Number_Segments.getCopyNumberSegmentsInSampleInStudyUsingGET(studyId=studyId,sampleId=sampleId).result()
    return copyNumberSegments

def getAllGenePanels():
    genePanels = cbioportal.Gene_Panels.getAllGenePanelsUsingGET().result()
    return genePanels

def getSpecificGenePanel(genePanelId):
    genePanel = cbioportal.Gene_Panels.getGenePanelUsingGET(genePanelId=genePanelId).result()
    return genePanel

def getAllGenes():
    genes = cbioportal.Genes.getAllGenesUsingGET().result()
    return genes

def getAliasForGene(geneId):
    alias = cbioportal.Genes.getAliasForGeneUsingGET(geneId=geneId).result()
    return alias

def getGene(geneId):
    gene = cbioportal.Genes.getGeneUsingGET(geneId=geneId).result()
    return gene

def getAllMolecularProfiles():
    molecularProfiles = cbioportal.Molecular_Profiles.getAllMolecularProfilesUsingGET().result()
    return molecularProfiles

def getMolecularProfile(molecularProfileId):
    molecularProfile = cbioportal.Molecular_Profiles.getMolecularProfileUsingGET(molecularProfileId=molecularProfileId).result()
    return molecularProfile

def getMolecularProfileInStudy(studyId, molecularProfileId):
    molecularProfile = cbioportal.Molecular_Profiles.getMolecularProfileInStudyUsingGET(studyId=studyId,molecularProfileId=molecularProfileId).result()
    return molecularProfile

