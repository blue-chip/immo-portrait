-- source: https://donnees.montreal.ca/dataset/unites-evaluation-fonciere

create table public.unites_evaluation_fonciere (
    id_uev bigint
    , civique_debut int
    , civique_fin int
    , nom_rue varchar
    , suite_debut varchar
    , municipalite int
    , etage_hors_sol int
    , nombre_logement int
    , annee_construction int
    , code_utilisation int
    , lettre_debut varchar
    , lettre_fin varchar
    , libelle_utilisation varchar
    , categorie_uef varchar
    , matricule83 int
    , superficie_terrain int
    , superficie_batiment int
    , no_arrond_ile_cum varchar
)
;
