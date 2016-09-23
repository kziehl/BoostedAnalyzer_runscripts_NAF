outpath='/nfs/dust/cms/user/kelmorab/samples8019/' # path of output of analyzer
scriptpath='scriptsSep15' # folder containing shell scripts that will have to be run on cluster
samplelist='SampleListJul18.csv' # samples list
dataset_column='boosted_dataset' # run on the column with dataset or boosted_dataset?
cmsswcfgpath='//nfs/dust/cms/user/kelmorab/CMSSW_8_0_19/src/BoostedTTH/BoostedAnalyzer/test/boostedAnalysis_karim_cfg.py'
cmsswpath='/nfs/dust/cms/user/kelmorab/CMSSW_8_0_19'
dbs="prod/phys03" # dbs instance: boosted miniaod is in prod/phys03, standard miniaod in prod/global
min_events_per_job=50000 # min number of events per job 
systematics=True # create extra trees with JES/JER systematics?
isBoostedMiniAOD=True # do the inputs contain fat jets?
analysisType='SL' # this is usually SL