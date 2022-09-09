from bravado.client import SwaggerClient as bravado_client

# This is the initialization of many of the data sources that we will need
cbioportal = bravado_client.from_url('https://www.cbioportal.org/api/v2/api-docs', 
    config={"validate_requests":False,"validate_responses":False,"validate_swagger_spec": False,})

def return_to_dict_converter(return_type,return_list):
    if type(return_list) == list:
        if return_type == 'dict':
            return_list_dict = []
            for return_item in return_list:
                return_item_dict = {}
                for att in dir(return_item):
                    return_item_dict[att] = getattr(return_item, att)
                return_list_dict.append(return_item_dict)
            return return_list_dict
        elif return_type == 'native':
            return return_list
    else:
        if return_type == 'dict':
            return_dict = {}
            for att in dir(return_list):
                return_dict[att] = getattr(return_list, att)
            return return_dict
        elif return_type == 'native':
            return return_list

#Fetch all of the studies
def getAllStudies(return_type = 'dict'): #I assume the end user will prefer a dictionary object
    studies = cbioportal.Studies.getAllStudiesUsingGET().result()
    return return_to_dict_converter(return_type,studies)

def getSpecificStudy(studyId, return_type = 'dict'):
    study = cbioportal.Studies.getStudyUsingGET(studyId=studyId).result()
    return return_to_dict_converter(return_type, study)

## verify that this works - couldn't get a non empty list return
def getStudyTags(studyId,return_type = 'dict'):
    studyTags = cbioportal.Studies.getTagsUsingGET(studyId=studyId).result()
    return return_to_dict_converter(return_type,studyTags)

def getAllCancerTypes(return_type = 'dict'):
    cancerTypes = cbioportal.Cancer_Types.getAllCancerTypesUsingGET().result()
    return return_to_dict_converter(return_type,cancerTypes)

def getCancerByID(cancerTypeId, return_type = 'dict'):
    cancerType = cbioportal.Cancer_Types.getCancerTypeUsingGET(cancerTypeId=cancerTypeId).result()
    return return_to_dict_converter(return_type,cancerType)

def getAllClinicalAttributes(return_type = 'dict'):
    clinicalAttributes = cbioportal.Clinical_Attributes.getAllClinicalAttributesUsingGET().result()
    return return_to_dict_converter(return_type, clinicalAttributes)

def getClinicalAttributesByStudyId(studyId, return_type = 'dict'):
    clinicalAttributes = cbioportal.Clinical_Attributes.getAllClinicalAttributesInStudyUsingGET(studyId=studyId).result()
    return return_to_dict_converter(return_type,clinicalAttributes)

def getClinicalAttributeInStudy(studyId, clinicalAttributeId, return_type = 'dict'):
    clinicalAttributes = cbioportal.Clinical_Attributes.getClinicalAttributeInStudyUsingGET(clinicalAttributeId=clinicalAttributeId,studyId=studyId).result()
    return return_to_dict_converter(return_type, clinicalAttributes)

def getAllClinicalDataInStudy(studyId, return_type = 'dict'):
    clinicalData = cbioportal.Clinical_Data.getAllClinicalDataInStudyUsingGET(studyId=studyId).result()
    return return_to_dict_converter(return_type,clinicalData)

def getAllClinicalDataOfPatientInStudy(studyId, patientId, return_type = 'dict'):
    clinicalData = cbioportal.Clinical_Data.getAllClinicalDataOfPatientInStudyUsingGET(studyId=studyId,patientId=patientId).result()
    return return_to_dict_converter(return_type,clinicalData)

def getAllClinicalDataOfSampleInStudy(studyId, sampleId, return_type = 'dict'):
    clinicalData = cbioportal.Clinical_Data.getAllClinicalDataOfSampleInStudyUsingGET(studyId=studyId,sampleId=sampleId).result()
    return return_to_dict_converter(return_type,clinicalData)

def getCopyNumberSegmentsInSampleInStudy(studyId, sampleId, return_type = 'dict'):
    copyNumberSegments = cbioportal.Copy_Number_Segments.getCopyNumberSegmentsInSampleInStudyUsingGET(studyId=studyId,sampleId=sampleId,).result()
    return return_to_dict_converter(return_type,copyNumberSegments)

def getAllGenePanels(return_type = 'dict'):
    genePanels = cbioportal.Gene_Panels.getAllGenePanelsUsingGET().result()
    return return_to_dict_converter(return_type,genePanels)

def getSpecificGenePanel(genePanelId, return_type = 'dict'):
    genePanel = cbioportal.Gene_Panels.getGenePanelUsingGET(genePanelId=genePanelId).result()
    return return_to_dict_converter(return_type, genePanel)

def getAllGenes(return_type = 'dict'):
    genes = cbioportal.Genes.getAllGenesUsingGET().result()
    return return_to_dict_converter(return_type, genes)

def getAliasForGene(geneId, return_type = 'dict'):
    alias = cbioportal.Genes.getAliasForGeneUsingGET(geneId=geneId).result()
    return return_to_dict_converter(return_type, alias)

def getGene(geneId, return_type = 'dict'):
    gene = cbioportal.Genes.getGeneUsingGET(geneId=geneId).result()
    return return_to_dict_converter(return_type, gene)

def getAllMolecularProfiles(return_type = 'dict'):
    molecularProfiles = cbioportal.Molecular_Profiles.getAllMolecularProfilesUsingGET().result()
    return return_to_dict_converter(return_type,molecularProfiles)

def getMolecularProfile(molecularProfileId, return_type = 'dict'):
    molecularProfile = cbioportal.Molecular_Profiles.getMolecularProfileUsingGET(molecularProfileId=molecularProfileId).result()
    return return_to_dict_converter(return_type,molecularProfile)

def getMolecularProfilesInStudy(studyId,return_type = 'dict'):
    molecularProfiles = cbioportal.Molecular_Profiles.getAllMolecularProfilesInStudyUsingGET(studyId=studyId).result()
    return return_to_dict_converter(return_type,molecularProfiles)

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
    return return_to_dict_converter(return_type,mutations)

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


#### POST FUNCTIONS ####

def GetPatientClinicalDataForSpecificStudyPOST(studyId, attributeIdsList, patientIdsList, projection = 'SUMMARY', return_type = 'dict'):
    clinicalDict = {
        "attributeIds": attributeIdsList,
        "ids": patientIdsList
    }
    clinicalAttributesList = cbioportal.Clinical_Data.fetchAllClinicalDataInStudyUsingPOST(
        clinicalDataSingleStudyFilter = clinicalDict,
        projection = projection,
        clinicalDataType = 'PATIENT',
        studyId = studyId
    ).result()
    if return_type == 'dict':
        clinicalAttributesList_list = []
        for clinicalAttributes in clinicalAttributesList:
            clinicalAttributes_dict = {}
            for att in dir(clinicalAttributes):
                clinicalAttributes_dict[att] = getattr(clinicalAttributes, att)
            clinicalAttributesList_list.append(clinicalAttributes_dict)
        return clinicalAttributesList_list
    elif(return_type == 'native'):
        return clinicalAttributesList

def getClinicalAttributesForSeveralPatientsPOST(studyId, attributeIdsList, sampleIdsList, projection = 'SUMMARY', return_type = 'dict'):
    clinicalDict = {
        "attributeIds": attributeIdsList,
        "ids": sampleIdsList
    }
    clinicalAttributesList = cbioportal.Clinical_Data.fetchAllClinicalDataInStudyUsingPOST(
        clinicalDataSingleStudyFilter = clinicalDict,
        projection = projection,
        clinicalDataType = 'SAMPLE',
        studyId = studyId
    ).result()
    if return_type == 'dict':
        clinicalAttributesList_list = []
        for clinicalAttributes in clinicalAttributesList:
            clinicalAttributes_dict = {}
            for att in dir(clinicalAttributes):
                clinicalAttributes_dict[att] = getattr(clinicalAttributes, att)
            clinicalAttributesList_list.append(clinicalAttributes_dict)
        return clinicalAttributesList_list
    elif(return_type == 'native'):
        return clinicalAttributesList

def getClinicalAtrributesFromSeveralStudiesPOST(studyidsList, return_type = 'dict'):
    clinicalAttributesList = cbioportal.Clinical_Attributes.fetchClinicalAttributesUsingPOST(
        studyIds = studyidsList
    ).result()
    if return_type == 'dict':
        clinicalAttributesList_list = []
        for clinicalAttributes in clinicalAttributesList:
            clinicalAttributes_dict = {}
            for att in dir(clinicalAttributes):
                clinicalAttributes_dict[att] = getattr(clinicalAttributes, att)
            clinicalAttributesList_list.append(clinicalAttributes_dict)
        return clinicalAttributesList_list
    elif(return_type == 'native'):
        return clinicalAttributesList

def getSeveralClinicalAttributesFromDifferentStudiesAndPatients(attributesIdList, patientStudyDictList, projection = 'SUMMARY', return_type = 'dict'):
    clinicalAttributesList = cbioportal.Clinical_Data.fetchClinicalDataUsingPOST(
        clinicalDataMultiStudyFilter = {
            "attributeIds": attributesIdList,
            "identifiers": patientStudyDictList
        },
        clinicalDataType = 'PATIENT',
        projection = projection
    ).result()
    if return_type == 'dict':
        clinicalAttributesList_list = []
        for clinicalAttributes in clinicalAttributesList:
            clinicalAttributes_dict = {}
            for att in dir(clinicalAttributes):
                clinicalAttributes_dict[att] = getattr(clinicalAttributes, att)
            clinicalAttributesList_list.append(clinicalAttributes_dict)
        return clinicalAttributesList_list
    elif(return_type == 'native'):
        return clinicalAttributesList

def getMolecularProfilesForSpecificEntrezIDPOST(entrezGeneIds,molecularProfileIdsList,projection='SUMMARY',return_type='dict'):
    molecularDataMultipleStudyFilter = {
        "entrezGeneIds":[
            entrezGeneIds
        ],
        "molecularProfileIds": molecularProfileIdsList 
    }
    molecularProfileReturns = cbioportal.Molecular_Data.fetchMolecularDataInMultipleMolecularProfilesUsingPOST(molecularDataMultipleStudyFilter = molecularDataMultipleStudyFilter, projection = projection).result()
    if return_type == 'dict':
        molecularProfileReturns_list = []
        for molecularProfileReturn in molecularProfileReturns:
            molecularProfileReturn_dict = {}
            for att in dir(molecularProfileReturn):
                molecularProfileReturn_dict[att] = getattr(molecularProfileReturn, att)
            molecularProfileReturns_list.append(molecularProfileReturn_dict)
        return molecularProfileReturns_list
    elif (return_type == 'native'):
        return molecularProfileReturns

def getMolecularProfilesForListOfMolecularProfileIds(molecularProfileIdsList,projection='SUMMARY',return_type='dict'):
    molecularProfileFilter = {
        'molecularProfileIds': molecularProfileIdsList
    }
    molecularProfileReturns = cbioportal.Molecular_Profiles.fetchMolecularProfilesUsingPOST(molecularProfileFilter = molecularProfileFilter, projection = projection).result()
    if return_type == 'dict':
        molecularProfileReturns_list = []
        for molecularProfileReturn in molecularProfileReturns:
            molecularProfileReturn_dict = {}
            for att in dir(molecularProfileReturn):
                molecularProfileReturn_dict[att] = getattr(molecularProfileReturn, att)
            molecularProfileReturns_list.append(molecularProfileReturn_dict)
        return molecularProfileReturns_list
    elif (return_type == 'native'):
        return molecularProfileReturns

def getMolecularProfilesForListOfStudyIds(studyIdsList,projection='SUMMARY',return_type='dict'):
    molecularProfileFilter = {
        'studyIds': studyIdsList
    }
    molecularProfileReturns = cbioportal.Molecular_Profiles.fetchMolecularProfilesUsingPOST(molecularProfileFilter = molecularProfileFilter, projection = projection).result()
    if return_type == 'dict':
        molecularProfileReturns_list = []
        for molecularProfileReturn in molecularProfileReturns:
            molecularProfileReturn_dict = {}
            for att in dir(molecularProfileReturn):
                molecularProfileReturn_dict[att] = getattr(molecularProfileReturn, att)
            molecularProfileReturns_list.append(molecularProfileReturn_dict)
        return molecularProfileReturns_list
    elif (return_type == 'native'):
        return molecularProfileReturns

def fetchMutationsInMolecularProfile(entrezGeneIdsListList,sampleIdsList,molecularProfileId, return_type = 'dict'):
    mutationFilter = {
        "entrezGeneIds": entrezGeneIdsListList,
        "sampleIds": sampleIdsList
    }
    mutationList = cbioportal.MolecularProfiles.fetchMolecularProfilesUsingPOST(molecularProfileId=molecularProfileId,mutationFilter=mutationFilter).result()
    if return_type == 'dict':
        mutationList_list = []
        for mutation in mutationList:
            mutation_dict = {}
            for att in dir(mutation):
                mutation_dict[att] = getattr(mutation, att)
            mutationList_list.append(mutation_dict)
        return mutationList_list
    elif (return_type == 'native'):
        return mutationList

##mutations fetch multiple profiles endpoint next
def fetchMutationsInMultipleMolecularProfilesPOST(entrezGeneIdsList, molecularProfileIdsList, return_type = 'dict'):
    mutationMultipleStudyFilter = {
        "entrezGeneIds": entrezGeneIdsList,
        "molecularProfileIds": molecularProfileIdsList
    }
    mutationList = cbioportal.Mutations.fetchMutationsInMultipleMolecularProfilesUsingPOST(mutationMultipleStudyFilter = mutationMultipleStudyFilter).result()
    if return_type == 'dict':
        mutationList_list = []
        for mutation in mutationList:
            mutation_dict = {}
            for att in dir(mutation):
                mutation_dict[att] = getattr(mutation, att)
            mutationList_list.append(mutation_dict)
        return mutationList_list
    elif (return_type == 'native'):
        return mutationList

def fetchDiscreteCopyNumberAlterationsPOST(entrezGeneIdsList,sampleIdsList, molecularProfileId,discreteCopyNumberEventType = 'ALL', projection='SUMMARY',return_type = 'dict'):
    discreteCopyNumberFilter = {
        "entrezGeneIds": entrezGeneIdsList,
        "sampleIds": sampleIdsList
    }
    discreteCopyNumberAltreations = cbioportal.Discrete_Copy_Number_Alterations.fetchDiscreteCopyNumbersInMolecularProfileUsingPOST(molecularProfileId=molecularProfileId,discreteCopyNumberFilter=discreteCopyNumberFilter,discreteCopyNumberEventType=discreteCopyNumberEventType,projection=projection).result()
    return return_to_dict_converter(return_type,discreteCopyNumberAltreations)

def fetchMultipleGenesPOST(entrezGeneIdsList,return_type = 'dict'):
    geneList = cbioportal.Genes.fetchGenesUsingPOST(geneIds=entrezGeneIdsList).result()
    return return_to_dict_converter(return_type,geneList)

def fetchGenePanelsFromMultipleMolecularProfileIdsPOST(molecularProfileIdsList,return_type = 'dict'):
    genePanelFilter = {
        'molecularProfileIds': molecularProfileIdsList
    }
    genePanelList = cbioportal.Gene_Panels.fetchGenePanelDataInMultipleMolecularProfilesUsingPOST(genePanelDataMultipleStudyFilter = genePanelFilter).result()
    return return_to_dict_converter(return_type, genePanelList)

def fetchListOfGenePanelsPOST(genePanelIdList, return_type='dict'):
    genePanels = cbioportal.Gene_Panels.fetchGenePanelsUsingPOST(genePanelIds=genePanelIdList).result()
    return return_to_dict_converter(return_type, genePanels)

#generic assays

def getGenericAssayMetaListGET(molecularProfileId, return_type = 'dict'):
    genericAssayMetaList = cbioportal.Generic_Assays.getGenericAssayMetaUsingGET(molecularProfileId=molecularProfileId).result()
    return return_to_dict_converter(return_type,genericAssayMetaList)

def getGenericAssayUsingGenericAssaayStableID(stableId, return_type = 'dict'):
    genericAssay = cbioportal.Generic_Assays.getGenericAssayMeta_gaUsingGET(genericAssayStableId=stableId).result()
    return return_to_dict_converter(return_type,genericAssay)

def fetchMultipleGenericAssayUsingPost(molecularProfileIdsLIST, genericAssayStableIdsLIST, return_type = 'dict'):
    genericAssayMetaFilter = {
        'molecularProfileIds': molecularProfileIdsLIST,
        'genericAssayStableIds': genericAssayStableIdsLIST
    }
    genericAssayList = cbioportal.Generic_Assays.fetchGenericAssayMetaUsingPOST(genericAssayMetaFilter = genericAssayMetaFilter).result()
    return return_to_dict_converter(return_type,genericAssayList)

#treatements



#structural variants
