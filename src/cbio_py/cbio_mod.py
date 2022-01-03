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

def getSpecificStudy(studyId, return_type = 'dict'):
    study = cbioportal.Studies.getStudyUsingGET(studyId=studyId).result()
    if return_type == 'dict':
        study_dict = {}
        for att in dir(study):
            study_dict[att] = getattr(study, att)
        return study_dict
    elif(return_type == 'native'):
        return study

def getStudyTags(studyId,return_type = 'dict'):
    studyTags = cbioportal.Studies.getTagsUsingGET(studyId=studyId).result()
    if return_type == 'dict':
        studyTags_list = []
        for studyTag in studyTags:
            studyTag_dict = {}
            for att in dir(studyTag):
                studyTag_dict[att] = getattr(studyTag, att)
            studyTags_list.append(studyTag_dict)
        return studyTags_list
    elif(return_type == 'native'):
        return studyTags

def getAllCancerTypes(return_type = 'dict'):
    cancerTypes = cbioportal.Cancer_Types.getAllCancerTypesUsingGET().result()
    if return_type == 'dict':
        cancerTypes_list = []
        for cancerType in cancerTypes:
            cancerType_dict = {}
            for att in dir(cancerType):
                cancerType_dict[att] = getattr(cancerType, att)
            cancerTypes_list.append(cancerType_dict)
        return cancerTypes_list
    elif(return_type == 'native'):
        return cancerTypes

def getCancerByID(cancerTypeId, return_type = 'dict'):
    cancerType = cbioportal.Cancer_Types.getCancerTypeUsingGET(cancerTypeId=cancerTypeId).result()
    if return_type == 'dict':
        cancerType_dict = {}
        for att in dir(cancerType):
            cancerType_dict[att] = getattr(cancerType, att)
        return cancerType_dict
    elif(return_type == 'native'):
        return cancerType

def getAllClinicalAttributes(return_type = 'dict'):
    clinicalAttributes = cbioportal.Clinical_Attributes.getAllClinicalAttributesUsingGET().result()
    if return_type == 'dict':
        clinicalAttributes_list = []
        for clinicalAttribute in clinicalAttributes:
            clinicalAttribute_dict = {}
            for att in dir(clinicalAttribute):
                clinicalAttribute_dict[att] = getattr(clinicalAttribute, att)
            clinicalAttributes_list.append(clinicalAttribute_dict)
        return clinicalAttributes_list
    elif(return_type == 'native'):
        return clinicalAttributes

def getClinicalAttributesByStudyId(studyId, return_type = 'dict'):
    clinicalAttributes = cbioportal.Clinical_Attributes.getAllClinicalAttributesInStudyUsingGET(studyId=studyId).result()
    if return_type == 'dict':
        clinicalAttributes_list = []
        for clinicalAttribute in clinicalAttributes:
            clinicalAttribute_dict = {}
            for att in dir(clinicalAttribute):
                clinicalAttribute_dict[att] = getattr(clinicalAttribute, att)
            clinicalAttributes_list.append(clinicalAttribute_dict)
        return clinicalAttributes_list
    elif(return_type == 'native'):
        return clinicalAttributes

def getClinicalAttributeInStudy(studyId, clinicalAttributeId, return_type = 'dict'):
    clinicalAttributes = cbioportal.Clinical_Attributes.getClinicalAttributeInStudyUsingGET(clinicalAttributeId=clinicalAttributeId,studyId=studyId).result()
    if return_type == 'dict':
        clinicalAttribute_dict = {}
        for att in dir(clinicalAttributes):
            clinicalAttribute_dict[att] = getattr(clinicalAttributes, att)
        return clinicalAttribute_dict
    elif(return_type == 'native'):
        return clinicalAttributes

def getAllClinicalDataInStudy(studyId, return_type = 'dict'):
    clinicalData = cbioportal.Clinical_Data.getAllClinicalDataInStudyUsingGET(studyId=studyId).result()
    if return_type == 'dict':
        clinicalData_list = []
        for clinicalData in clinicalData:
            clinicalData_dict = {}
            for att in dir(clinicalData):
                clinicalData_dict[att] = getattr(clinicalData, att)
            clinicalData_list.append(clinicalData_dict)
        return clinicalData_list
    elif(return_type == 'native'):
        return clinicalData

def getAllClinicalDataOfPatientInStudy(studyId, patientId, return_type = 'dict'):
    clinicalData = cbioportal.Clinical_Data.getAllClinicalDataOfPatientInStudyUsingGET(studyId=studyId,patientId=patientId).result()
    if return_type == 'dict':
        clinicalData_list = []
        for clinicalData in clinicalData:
            clinicalData_dict = {}
            for att in dir(clinicalData):
                clinicalData_dict[att] = getattr(clinicalData, att)
            clinicalData_list.append(clinicalData_dict)
        return clinicalData_list
    elif(return_type == 'native'):
        return clinicalData

def getAllClinicalDataOfSampleInStudy(studyId, sampleId, return_type = 'dict'):
    clinicalData = cbioportal.Clinical_Data.getAllClinicalDataOfSampleInStudyUsingGET(studyId=studyId,sampleId=sampleId).result()
    if return_type == 'dict':
        clinicalData_list = []
        for clinicalData in clinicalData:
            clinicalData_dict = {}
            for att in dir(clinicalData):
                clinicalData_dict[att] = getattr(clinicalData, att)
            clinicalData_list.append(clinicalData_dict)
        return clinicalData_list
    elif(return_type == 'native'):
        return clinicalData 

def getCopyNumberSegmentsInSampleInStudy(studyId, sampleId, return_type = 'dict'):
    copyNumberSegments = cbioportal.Copy_Number_Segments.getCopyNumberSegmentsInSampleInStudyUsingGET(studyId=studyId,sampleId=sampleId).result()
    if return_type == 'dict':
        copyNumberSegments_list = []
        for copyNumberSegment in copyNumberSegments:
            copyNumberSegment_dict = {}
            for att in dir(copyNumberSegment):
                copyNumberSegment_dict[att] = getattr(copyNumberSegment, att)
            copyNumberSegments_list.append(copyNumberSegment_dict)
        return copyNumberSegments_list
    elif(return_type == 'native'):
        return copyNumberSegments

def getAllGenePanels(return_type = 'dict'):
    genePanels = cbioportal.Gene_Panels.getAllGenePanelsUsingGET().result()
    if return_type == 'dict':
        genePanels_list = []
        for genePanel in genePanels:
            genePanel_dict = {}
            for att in dir(genePanel):
                genePanel_dict[att] = getattr(genePanel, att)
            genePanels_list.append(genePanel_dict)
        return genePanels_list
    elif(return_type == 'native'):
        return genePanels

def getSpecificGenePanel(genePanelId, return_type = 'dict'):
    genePanel = cbioportal.Gene_Panels.getGenePanelUsingGET(genePanelId=genePanelId).result()
    if return_type == 'dict':
        genePanel_dict = {}
        for att in dir(genePanel):
            genePanel_dict[att] = getattr(genePanel, att)
        return genePanel_dict
    elif(return_type == 'native'):
        return genePanel

def getAllGenes(return_type = 'dict'):
    genes = cbioportal.Genes.getAllGenesUsingGET().result()
    if return_type == 'dict':
        genes_list = []
        for gene in genes:
            gene_dict = {}
            for att in dir(gene):
                gene_dict[att] = getattr(gene, att)
            genes_list.append(gene_dict)
        return genes_list
    elif(return_type == 'native'):
        return genes

def getAliasForGene(geneId, return_type = 'dict'):
    alias = cbioportal.Genes.getAliasForGeneUsingGET(geneId=geneId).result()
    if return_type == 'dict':
        alias_dict = {}
        for att in dir(alias):
            alias_dict[att] = getattr(alias, att)
        return alias_dict
    elif(return_type == 'native'):
        return alias

def getGene(geneId, return_type = 'dict'):
    gene = cbioportal.Genes.getGeneUsingGET(geneId=geneId).result()
    if return_type == 'dict':
        gene_dict = {}
        for att in dir(gene):
            gene_dict[att] = getattr(gene, att)
        return gene_dict
    elif(return_type == 'native'):
        return gene

def getAllMolecularProfiles(return_type = 'dict'):
    molecularProfiles = cbioportal.Molecular_Profiles.getAllMolecularProfilesUsingGET().result()
    if return_type == 'dict':
        molecularProfiles_list = []
        for molecularProfile in molecularProfiles:
            molecularProfile_dict = {}
            for att in dir(molecularProfile):
                molecularProfile_dict[att] = getattr(molecularProfile, att)
            molecularProfiles_list.append(molecularProfile_dict)
        return molecularProfiles_list
    elif(return_type == 'native'):
        return molecularProfiles

def getMolecularProfile(molecularProfileId, return_type = 'dict'):
    molecularProfile = cbioportal.Molecular_Profiles.getMolecularProfileUsingGET(molecularProfileId=molecularProfileId).result()
    if return_type == 'dict':
        molecularProfile_dict = {}
        for att in dir(molecularProfile):
            molecularProfile_dict[att] = getattr(molecularProfile, att)
        return molecularProfile_dict
    elif(return_type == 'native'):
        return molecularProfile

def getMolecularProfileInStudy(studyId, molecularProfileId, return_type = 'dict'):
    molecularProfile = cbioportal.Molecular_Profiles.getMolecularProfileInStudyUsingGET(studyId=studyId,molecularProfileId=molecularProfileId).result()
    if return_type == 'dict':
        molecularProfile_dict = {}
        for att in dir(molecularProfile):
            molecularProfile_dict[att] = getattr(molecularProfile, att)
        return molecularProfile_dict
    elif(return_type == 'native'):
        return molecularProfile

# appending _all and _mutations to study id here 
def getMutationsInMolecularProfile(molecularProfileId, sampleListId, projection='DETAILED', return_type = 'dict', append='yes'):
    if append == 'yes':
        molecularProfileId = molecularProfileId + '_mutations'
        sampleListId = sampleListId + '_all'
    else:
        molecularProfileId = molecularProfileId
        sampleListId = sampleListId 
    mutations = cbioportal.Mutations.getMutationsInMolecularProfileBySampleListIdUsingGET(
        molecularProfileId=molecularProfileId,sampleListId = sampleListId, projection=projection).result()
    if return_type == 'dict':
        mutations_list = []
        for mutation in mutations:
            mutation_dict = {}
            for att in dir(mutation):
                mutation_dict[att] = getattr(mutation, att)
            mutations_list.append(mutation_dict)
        return mutations_list
    elif(return_type == 'native'):
        return mutations

def getAllPatients(return_type = 'dict'):
    patients = cbioportal.Patients.getAllPatientsUsingGET().result()
    if return_type == 'dict':
        patients_list = []
        for patient in patients:
            patient_dict = {}
            for att in dir(patient):
                patient_dict[att] = getattr(patient, att)
            patients_list.append(patient_dict)
        return patients_list
    elif(return_type == 'native'):
        return patients

def getAllPatientsInStudy(studyId, return_type = 'dict'):
    patients = cbioportal.Patients.getAllPatientsInStudyUsingGET(studyId=studyId).result()
    if return_type == 'dict':
        patients_list = []
        for patient in patients:
            patient_dict = {}
            for att in dir(patient):
                patient_dict[att] = getattr(patient, att)
            patients_list.append(patient_dict)
        return patients_list
    elif(return_type == 'native'):
        return patients

def getPatientInStudy(studyId, patientId, return_type = 'dict'):
    patient = cbioportal.Patients.getPatientInStudyUsingGET(studyId=studyId,patientId=patientId).result()
    if return_type == 'dict':
        patient_dict = {}
        for att in dir(patient):
            patient_dict[att] = getattr(patient, att)
        return patient_dict
    elif(return_type == 'native'):
        return patient

def getAllSamplesList(return_type = 'dict'):
    samplesList = cbioportal.Sample_Lists.getAllSampleListsUsingGET().result()
    if return_type == 'dict':
        samplesList_list = []
        for samplesList in samplesList:
            samplesList_dict = {}
            for att in dir(samplesList):
                samplesList_dict[att] = getattr(samplesList, att)
            samplesList_list.append(samplesList_dict)
        return samplesList_list
    elif(return_type == 'native'):
        return samplesList

def getSpecificSampleList(sampleListId, return_type = 'dict'):
    samplesList = cbioportal.Sample_Lists.getSampleListUsingGET(sampleListId=sampleListId).result()
    if return_type == 'dict':
        samplesList_dict = {}
        for att in dir(samplesList):
            samplesList_dict[att] = getattr(samplesList, att)
        return samplesList_dict
    elif(return_type == 'native'):
        return samplesList

def getSampleListInStudy(studyId, sampleListId, return_type = 'dict'):
    samplesList = cbioportal.Sample_Lists.getSampleListInStudyUsingGET(studyId=studyId,sampleListId=sampleListId).result()
    if return_type == 'dict':
        samplesList_dict = {}
        for att in dir(samplesList):
            samplesList_dict[att] = getattr(samplesList, att)
        return samplesList_dict
    elif(return_type == 'native'):
        return samplesList

def getAllSamplesInStudy(studyId, return_type = 'dict'):
    samples = cbioportal.Samples.getAllSamplesInStudyUsingGET(studyId=studyId).result()
    if return_type == 'dict':
        samples_list = []
        for sample in samples:
            sample_dict = {}
            for att in dir(sample):
                sample_dict[att] = getattr(sample, att)
            samples_list.append(sample_dict)
        return samples_list
    elif(return_type == 'native'):
        return samples

def getAllSamplesOfPatientInStudy(studyId, patientId, return_type = 'dict'):
    samples = cbioportal.Samples.getAllSamplesOfPatientInStudyUsingGET(studyId=studyId,patientId=patientId).result()
    if return_type == 'dict':
        samples_list = []
        for sample in samples:
            sample_dict = {}
            for att in dir(sample):
                sample_dict[att] = getattr(sample, att)
            samples_list.append(sample_dict)
        return samples_list
    elif(return_type == 'native'):
        return samples

def getSampleInStudy(studyId, sampleId, return_type = 'dict'):
    sample = cbioportal.Samples.getSampleInStudyUsingGET(studyId=studyId,sampleId=sampleId).result()
    if return_type == 'dict':
        sample_dict = {}
        for att in dir(sample):
            sample_dict[att] = getattr(sample, att)
        return sample_dict
    elif(return_type == 'native'):
        return sample

def getSamplesByKeyword(keyword, return_type = 'dict'):
    samples = cbioportal.Samples.getSamplesByKeywordUsingGET(keyword=keyword).result()
    if return_type == 'dict':
        samples_list = []
        for sample in samples:
            sample_dict = {}
            for att in dir(sample):
                sample_dict[att] = getattr(sample, att)
            samples_list.append(sample_dict)
        return samples_list
    elif(return_type == 'native'):
        return samples

