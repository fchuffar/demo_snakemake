# demo_snakemake
A set of scripts to illustrate the use of snakemake


## Purpose

The objectives are:
i) introducing `Snakemake` using these supports:
    - https://slides.com/johanneskoester/deck-1
    - https://www.slideshare.net/slideshow/introduction-to-snakemake/83052693
    - https://moodle.france-bioinformatique.fr/pluginfile.php/346/course/section/47/13_tutoriel_snakemake.html#/
ii) introducing the CIMENT/GRICAD infrastructure using https://github.com/fchuffar/practicle_sessions/blob/master/ciment_infrastructure/ciment_infrastructure.odp
iii) put the concepts we've learned into practice through a few use cases.


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

When your account is becomed `Active`, connect to the cluster front-end as follows:

```
username=chuffarf
ssh -o ProxyCommand="ssh ${username}@access-gricad.univ-grenoble-alpes.fr -W %h:%p" dahu.univ-grenoble-alpes.fr
```

### Conda environement

Set up your conda environement as follow:

```
source /home/chuffarf/conda_config.sh
# conda create -n demosnakemake_env
# mamba install -c anaconda -c bioconda -c conda-forge -c r r-base snakemake=7.32.4 
conda activate demosnakemake_env
```

### Launch your first workflow

```
snakemake --forceall --dag -s 00_run_pipeline.py| dot -Tpdf > dag.pdf
snakemake --cores 4 -s 00_run_pipeline.py -pn
```

### Launch your second workflow
