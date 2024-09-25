# rule target:
#   threads: 1
#   input:
#     "sim_results_01.txt",
#     "sim_results_02.txt",
#     "sim_results_03.txt",
#   shell:"""
# echo "Tout est accompli." 
# """

# rule clean:
#   threads: 1
#   shell:"rm -Rf sim_results_*.txt"

# rule run_simulation:
#   output:"sim_results_{id}.txt",
#   threads: 1
#   shell:"""
# sleep 3
# echo $HOSTNAME > {output}
# """

localrules: target



import os 
import os.path

prefix = os.getcwd()

# simulator parameters

ncells  = ["100000"]
ncells  = ["100"]
mis = "1"
sijs = ["100"] 
ds = ["1.0"]
fs = ["50"]
lambs = ["1.0"]

gamma1s = ["0", "1"]
gamma2s = ["0", "500"]
seeds = ["0", "1", "2"]
# seeds = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

htmls = [f"{prefix}/mediation_analysis_lm_{ncell}_{i}_{sij}_{gamma1}_{gamma2}_{d}_{f}_{lamb}_rep{seed}.html" for ncell in ncells for i in mis for sij in sijs for gamma1 in gamma1s for gamma2 in gamma2s for d in ds for f in fs for lamb in lambs for seed in seeds]

print(htmls)
 
rule target:
  threads: 1
  message: "-- Execute the DAG. --"
  input:
    htmls
  shell:"""
RCODE="rmarkdown::render('metaanalysis.Rmd')"
echo $RCODE | Rscript -
echo "done." 
"""

rule mediation_analysis_lm:
    input:
      sim = "{prefix}/simulator.py",
      rmd = "{prefix}/mediation_analysis_lm.Rmd",
      par = "{prefix}/params.R",
    output:
      html     = "{prefix}/mediation_analysis_lm_{ncell}_{i}_{sij}_{gamma1}_{gamma2}_{d}_{f}_{lamb}_rep{seed}.html"    ,
      rout     = "{prefix}/mediation_analysis_lm_{ncell}_{i}_{sij}_{gamma1}_{gamma2}_{d}_{f}_{lamb}_rep{seed}.Rout"    ,
      sres    = "{prefix}/sim_res_{ncell}_{i}_{sij}_{gamma1}_{gamma2}_{d}_{f}_{lamb}_rep{seed}.txt",
      infos    = "{prefix}/infos_{ncell}_{i}_{sij}_{gamma1}_{gamma2}_{d}_{f}_{lamb}_rep{seed}.rds",
      exec    = "{prefix}/exectime_{ncell}_{i}_{sij}_{gamma1}_{gamma2}_{d}_{f}_{lamb}_rep{seed}.rds",
      fit    = "{prefix}/fitmed_{ncell}_{i}_{sij}_{gamma1}_{gamma2}_{d}_{f}_{lamb}_rep{seed}.rds",
    threads: 1
    shell:"""
export OMP_NUM_THREADS=1
# source /home/chuffarf/conda_config.sh
# conda activate demosnakemake_env

cd {wildcards.prefix}

RCODE="
  ncell = '{wildcards.ncell}'; i = '{wildcards.i}'; sij = '{wildcards.sij}'; gamma1 = '{wildcards.gamma1}'; gamma2 = '{wildcards.gamma2}'; d = '{wildcards.d}'; f = '{wildcards.f}'; lamb = '{wildcards.lamb}'; seed = {wildcards.seed}; source('params.R');
  rmarkdown::render('mediation_analysis_lm.Rmd', output_file=paste0('mediation_analysis_lm_', suffix, '.html'), intermediates_dir=paste0('tmp_', suffix))"
echo $RCODE | Rscript - 2>&1 > {output.rout}
"""

rule clean:
  threads: 1
  shell:"rm -Rf *.txt *.rds *.Rout *.html .snakemake"
