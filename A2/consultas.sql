
--- Índice de Desenvolvimento da Educação Básica - IDEB ---
SELECT * FROM `basedosdados.br_inep_ideb.brasil`  

SELECT ano,rede,ensino,anos_escolares,nota_saeb_matematica, nota_saeb_lingua_portuguesa, ideb 
FROM `basedosdados.br_inep_ideb.brasil` 
where ano >= 2019 and ano <= 2021 and rede = 'municipal' and anos_escolares = 'finais (6-9)'

---------------------------------------
SELECT * FROM `basedosdados.br_inep_saeb.dicionario`

SELECT * FROM `basedosdados.br_inep_saeb.proficiencia` 
select ano, sigla_uf, count(distinct id_aluno) FROM `basedosdados.br_inep_saeb.proficiencia` group by ano,sigla_uf having ano = 2019 or ano = 2021


SELECT * FROM `basedosdados.br_inep_ideb.uf`
SELECT * FROM `basedosdados.br_inep_ideb.municipio` 
SELECT * FROM `basedosdados.br_inep_ideb.regiao` 
SELECT * FROM `basedosdados.br_inep_ideb.escola

SELECT ano,
avg(taxa_aprovacao_ef) as media_aprovacao_ef,
avg(taxa_aprovacao_em) as media_aprovacao_em
FROM  `basedosdados.br_inep_indicadores_educacionais.brasil` as bd 
group by ano
having ano >= 2015 and ano <= 2021 
order by ano desc 

--- Indicadores Educacionais
SELECT * FROM `basedosdados.br_inep_indicadores_educacionais.uf` LIMIT 100
SELECT ano,sigla_uf,rede, taxa_abandono_em	 FROM `basedosdados.br_inep_indicadores_educacionais.uf` WHERE ano = 2020 and rede = 'total' and localizacao = 'total'



SELECT count(*) FROM  `basedosdados.br_inep_indicadores_educacionais.brasil` 
WHERE ano = 2019

SELECT ano,rede,sigla_uf,avg(tnr_em) as media_nao_resposta_em, avg(tnr_ef) as media_nao_resposta_ef FROM  `basedosdados.br_inep_indicadores_educacionais.uf` 
group by ano,rede,sigla_uf
having ano = 2020
order by ano 

--- Indicador Nível Socioeconômico (INSE) ---
SELECT * FROM `basedosdados.br_inep_indicador_nivel_socioeconomico.brasil` 
SELECT ano, sum(quantidade_alunos_inse) FROM `basedosdados.br_inep_indicador_nivel_socioeconomico.brasil` group by ano
SELECT ano, sum(quantidade_alunos_inse) FROM `basedosdados.br_inep_indicador_nivel_socioeconomico.uf` group by ano 
SELECT * FROM `basedosdados.br_inep_indicador_nivel_socioeconomico.municipio` 
SELECT * FROM `basedosdados.br_inep_indicador_nivel_socioeconomico.escola` 

SELECT * FROM `basedosdados.br_inep_indicador_nivel_socioeconomico.brasil` WHERE ano < 2021 

SELECT bd.ano,bd.sigla_uf,sum(quantidade_alunos_inse) FROM `basedosdados.br_inep_indicador_nivel_socioeconomico.escola` as bd left join `basedosdados.br_inep_ideb.escola` as ba on ba.id_escola = bd.id_escola group by bd.ano,bd.sigla_uf having ano = 2019

SELECT ano,sigla_uf,sum(quantidade_alunos_inse) as total_alunos 
FROM `basedosdados.br_inep_indicador_nivel_socioeconomico.uf` 
group by ano,sigla_uf 
having ano = 2021 or ano = 2019


--- Censo Escolar ---
SELECT * FROM `basedosdados.br_inep_censo_escolar.dicionario`  
SELECT * FROM `basedosdados.br_inep_censo_escolar.escola` 
SELECT * FROM `basedosdados.br_inep_censo_escolar.docente` 
SELECT * FROM `basedosdados.br_inep_censo_escolar.turma` 
SELECT count(*) FROM `basedosdados.br_inep_censo_escolar.matricula` 
where ano = 2020 
