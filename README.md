# demo_snakemake
A set of scripts to illustrate the use of snakemake


## Purpose

The objectives are:

i) Introducing `snakemake` using these supports:

    - https://slides.com/johanneskoester/deck-1
    - https://www.slideshare.net/slideshow/introduction-to-snakemake/83052693
    - https://moodle.france-bioinformatique.fr/pluginfile.php/346/course/section/47/13_tutoriel_snakemake.html#/

ii) Introducing the CIMENT/GRICAD infrastructure using https://github.com/fchuffar/practicle_sessions/blob/master/ciment_infrastructure/ciment_infrastructure.odp

iii) Put the concepts we've learned into practice through a few use cases.


## How to start?

### Create an account to access to the cluster

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
 

### Connection to the cluster (if needed)

Once your account has become active, log in to the cluster frontend as follows:

```
username=chuffarf
ssh -o ProxyCommand="ssh ${username}@access-gricad.univ-grenoble-alpes.fr -W %h:%p" dahu.univ-grenoble-alpes.fr
```

Then, submit an interactive (`-I`) job of 4 cores:

```
oarsub --project groupecalcul -C 26054906 -l nodes=1/core=4,walltime=1:00:00  -I
```

```

### Conda environement

Set up your conda environement as follow:

```
source /home/chuffarf/conda_config.sh
# conda create -n demosnakemake_env
conda activate demosnakemake_env
# mamba install -c anaconda -c bioconda -c conda-forge -c r r-base snakemake=7.32.4 python-kaleido tenacity plotly
# pip install smgantt==0.0.5
```

### Set up your working directory

```
# Retrieve script and material from github
git clone https://github.com/fchuffar/demo_snakemake.git
# Go to your workdir
cd demo_snakemake
```

### Launch your first workflow

```
snakemake --cores 4 -s 01st_workflow.py -pn
snakemake --forceall --dag -s 01st_workflow.py| dot -Tpdf > dag.pdf
smgantt
```

play with the core argument and the threads parameter of the workflow and observe behaviour


### Launch your second workflow
