# The following comments couldn't be translated into the new config version:

#save digis sim link and trigger infos

#save digis

import FWCore.ParameterSet.Config as cms

#Full Event content 
SimMuonFEVT = cms.PSet(
    outputCommands = cms.untracked.vstring('keep StripDigiSimLinkedmDetSetVector_simMuonCSCDigis_*_*', 
        'keep CSCDetIdCSCComparatorDigiMuonDigiCollection_simMuonCSCDigis_*_*', 
        'keep DTLayerIdDTDigiSimLinkMuonDigiCollection_simMuonDTDigis_*_*', 
        'keep RPCDigiSimLinkedmDetSetVector_simMuonRPCDigis_*_*')
)
#Full Event content with DIGI
SimMuonFEVTDIGI = cms.PSet(
    outputCommands = cms.untracked.vstring('keep *_simMuonCSCDigis_*_*', 
        'keep *_simMuonDTDigis_*_*', 
        'keep *_simMuonRPCDigis_*_*')
)
#RECO content
SimMuonRECO = cms.PSet(
    outputCommands = cms.untracked.vstring()
)
#AOD content
SimMuonAOD = cms.PSet(
    outputCommands = cms.untracked.vstring()
)


