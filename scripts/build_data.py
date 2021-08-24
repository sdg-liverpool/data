from sdg.open_sdg import open_sdg_build

def alter_meta(meta):
  for i in range(1,7):
    if 'source_organisation_'+str(i) in meta and meta['source_organisation_'+str(i)] != '':
      meta['source_active'+str(i)]=True
  return meta

open_sdg_build(config='config_data.yml', alter_meta=alter_meta)
