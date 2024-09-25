# demo_snakemake
A set of scripts to illustrate the use of snakemake


## Purpose

The objectives are:

i) Introducing `snakemake` using these supports:

    - https://slides.com/johanneskoester/deck-1
    - https://www.slideshare.net/slideshow/introduction-to-snakemake/83052693
    - https://moodle.france-bioinformatique.fr/pluginfile.php/346/course/section/47/13_tutoriel_snakemake.html#/

ii) Introducing the CIMENT/GRICAD infrastructure

iii) Put the concepts we've learned into practice through a few use cases.


## Create an account to access to the cluster

Open a PERSEUS account by clicking on the following link:  

  - https://perseus.univ-grenoble-alpes.fr/create-account/form
  - Choose a login following the recommendations
  - Use an institutional email address
  - Choose “formations” as your laboratory
  - Choose your contract and select a suitable end date
  - Choose a password
 
You will receive two emails: 

  - one to join a project, choose the appropriate project
  - one to validate your email, follow the procedure
 

## How to start? (180 seconds turorial)


### Connection to the cluster (if needed)

ciment_infrastructure (Figure)


Once your account has become active, log in to the cluster frontend as follows:

```
username=chuffarf
ssh -o ProxyCommand="ssh ${username}@access-gricad.univ-grenoble-alpes.fr -W %h:%p" dahu.univ-grenoble-alpes.fr
```

Then, submit an interactive (`-I`) job of 4 cores:

```
oarsub --project groupecalcul -l nodes=1/core=2,walltime=00:03:00 -t fat -I
oarsub --project groupecalcul -t inner=26054906 -l nodes=1/core=8,walltime=00:30:00 -I # mercr.
oarsub --project groupecalcul -t inner=26054914 -l nodes=1/core=8,walltime=00:30:00 -I # jeud.
oarsub --project groupecalcul -t inner=26054926 -l nodes=1/core=8,walltime=00:30:00 -I # vendr.
chandler
oarstat -u cougoulg
```

```

### Conda environment

Set up your conda environment as follow:

```
source /home/chuffarf/conda_config.sh
# conda create -n demosnakemake_env
conda activate demosnakemake_env
# mamba install -c anaconda -c bioconda -c conda-forge -c r r-base snakemake=7.32.4 python-kaleido tenacity plotly graphviz r-rmarkdown
# pip install smgantt==0.0.5
```

Ex: Set your own conda environment 

### Set up your working directory

```
# Retrieve script and material from github
git clone https://github.com/fchuffar/demo_snakemake.git
# Go to your workdir
cd demo_snakemake
```

### Launch your first workflow

```
snakemake clean -s 01st_workflow.py --cores 1 -rp
snakemake -s 01st_workflow.py --cores 2 -rpn
snakemake --forceall --dag -s 01st_workflow.py| dot -Tpdf > dag.pdf
smgantt
```

Ex: 

  - Reproduice the *180 seconds tutorial* section.
  - Enhance the *180 seconds tutorial* by adjusting snakemake `cores` argument and `threads` rule parameter. 
  - Comment.
  





### `02nd_worflow.py`

Extracts:

```
# DO NOT EXECUTE
localrules: target

import os 
import os.path
prefix = os.getcwd()

# simulator parameters
ncells  = ["100000"]
ncells  = ["1000"]
mis = "1"
sijs = ["100"] 
ds = ["1.0"]
fs = ["50"]
lambs = ["1.0"]

# parameter sweep
gamma1s = ["0", "1"]
gamma2s = ["0", "500"]
seeds = ["rep1", "rep2", "rep3"]
```

Launch it:

```
snakemake -s 02nd_worflow.py --cores 2 -rpn
snakemake --forceall --dag -s 02nd_worflow.py| dot -Tpdf > dag.pdf
smgantt


```


### 

