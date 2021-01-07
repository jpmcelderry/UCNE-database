Ultraconserved Non-coding Elements Database Usage

written by John McElderry

*WRITTEN USING*
jQuery
ajax
python3
python CGI
python mysql.connector

*USAGE*
The database is relatively straightforward to use. Fields can be mixed and matched for customized querying, and any field left blank simply won't be used as a filter. Note that the assemblies used when describing genome coordinates for human, mouse, and zebrafish are hg19, mm10, and danRer7 respectively. An explanation of the fields and their purpose:

UCNE id: 
the UCNE ID, according to UCNEbase IDs

UCNE name: 
the name of the UCNE, UCNE names in zebrafish and mice are identical to their human orthologs (though in some cases there may be only 1 human ortholog for several UCNEs due to gene duplications, which is common in zebrafish)

UCNE Regulatory Block: 
nearby UCNEs (in humans) that are thought to interact due to conserved synteny are referred to as UCNE Regulatory Blocks (UCRB) and are hypothesized to have a common regulatory function. Note that UCNE names contain an underscore, such as "FOXD3_Frederica". In this case the name before the underscore indicates the UCRB this UCNE is assigned to. If a UCNE simply contains "chr" where the UCRB name should be, then this UCNE has not been assigned a UCRB.

Organism:
the organism in which to search for UCNEs, set to all by default

Chromosome:
a specific chromosome to search in

between/and:
chromosome coordinates in which to search, which are treated as start and stop coordinates respectively, and are searched with operators >= and <= respectively. Users can specify only one of start and stop if desired, or both.

minimum identity:
a minimum identity between the UCNE and human ortholog. Note that human orthologs will always have 100% identity by definition, and thus this field is simply left blank in human UCNE entries.

minimum length:
minimum length of UCNEs

sort by:
select how you want the results sorted, by which column and, in the case of identity and length, how to order the results

If no parameters are set, the program will query only for human UCNEs to give the user a starting point from which to build a more specific query.

*OUTPUT*
The program will output a match count at the head of the search result as well as a table with results containing all fields. Tables can be copy pasted into excel or your text editor as a tsv.
