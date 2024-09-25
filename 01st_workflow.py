rule target:
  threads: 1
  input:
    "simu_result_01.txt",
    "simu_result_02.txt",
    "simu_result_03.txt",
    "simu_result_04.txt",
    "simu_result_05.txt",
    "simu_result_06.txt",
    "simu_result_07.txt",
    "simu_result_08.txt",
    "simu_result_09.txt",
    "simu_result_10.txt"
  shell:"""
echo "Tout est accompli." 
"""
localrules: target

rule run_simulation:
  output:"simu_result_{id}.txt",
  threads: 1
  shell:"""
sleep 2
echo $HOSTNAME > {output}
"""