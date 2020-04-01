# DBSCAN-SWA: rapid prophage detection and annotation
## Table of Contents
- [Background](#background)
- [Requirements](requirements)
- [Install](#install)
- [Usage](#usage)
- [Examples](#example)
- [Contributors](#contributors)
- [License](#license)
## Background
Bacteriophages are viruses that specifically infect bacteria and the infected bacteria are called bacterial hosts of the viruses. Passive replication of the bacteriophage genome relies on integrate into the host's chromosome and becoming a prophage. Prophages coexist and co-evolve with bacteria in the natural environment, having an impact on the entire ecological environment. Therefore, it is very essential to develop effective and accurate tools for identification of prophages. DBSCAN-SWA, a command line software tool developed to predict prophage regions in bacterial genomes, running faster than any previous tools and presenting great detection power based on the analysis using 184 manually curated prophages
## Requirements ##
The source code is written by python3. In addition, several tools have been applied in DBSCAN-SWA. Among these, Prokka requires installtion by users. <br>
First, please install the following python packages:

1. numpy
 
2. Biopython
 
3. sklearn

Second, please install the following tools:
1. Prokka in https://github.com/tseemann/prokka

## Install ##
#### Linux
- step1:Download the whole packages and partial profiles from [https://github.com/HIT-ImmunologyLab/DBSCAN-SWA](https://github.com/HIT-ImmunologyLab/DBSCAN-SWA)
- step2:add the [download_path]/bin to your environment.
- step3: test DBSCAN-SWA in command line
```
dbscan-swa --h
```
## Usage
DBSCAN-SWA is an integrated tool for detection of prophages, providing a series of analysis including ORF prediction and genome annotation, phage-like gene clusters detection, attachments site identification and infecting phages annotation
### Command line options

```
General:
--input <file name>        : Query phage file path: FASTA or GenBank file
--output <folder name>     : Output folder in which results will be stored
--prefix <prefix>     : default: bac:

Phage Clustering:
--evalue <x>               : maximal E-value of searching for homology virus proteins from viral UniProt TrEML database. default:1e-7
--min_protein_num <x>      : optional,the minimal number of proteins forming a phage cluster in DBSCAN, default:6
--protein_number <x>       : optional,the number of expanding proteins when finding prophage att sites, default:10

Phage Annotation:
--add_annotation <options> : optional,default:PGPD,
   1.PGPD: a phage genome and protein database,
   2.phage_path:specified phage genome in FASTA or GenBank format to detect whether the phage infects the query bacteria
   3.none:no phage annotation
--per <x>                  : Minimal % percentage of hit proteins on hit prophage region(default:30)
--idn <x>                  : Minimal % identity of hit region on hit prophage region by making blastn(default:70)
-cov <x>                   : Minimal % coverage of hit region on hit prophage region by making blastn(default:30)
```
### Start DBSCAN-SWA
1.predict prophages of query bacterium with default parameters:

```
dbscan-swa --input <bac_path> --output <outdir> --prefix <prefix>
```
2. predict prophages of query bacterium and no phage annotation:
```
dbscan-swa --input <bac_path> --output <outdir> --prefix <prefix> --add_annotation nonne
```
3. predict prophages of query bacterium and detect the bacterium-phage interaction between the query bacterium and query phage:
```
dbscan-swa --input <bac_path> --output <outdir> --prefix <prefix> --add_annotation <phage_path>
```
## Visualizations
You can find a directory named "test" in the DBSCAN-SWA package. The following visualzations come from the predicted results of NC\_009632
