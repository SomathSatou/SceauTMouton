include "globals.mzn";

%La seul variable : le nombre de mouton.
int: nbr_m;
int: taille_ligne = (nbr_m*2)+1;
enum etat_case = {noir,vide,blanc};

int: max_step = 14;

array[1..max_step,1..taille_ligne] of var etat_case: etat;
array[1..max_step] of var 1..taille_ligne: mouton_sauteur;
array[1..max_step] of var 1..taille_ligne: case_arrive;
array[1..max_step] of var 0..1: unsolved_step;

%Les moutons commencent chacun dans leur coin.
constraint forall(c in 1..nbr_m)(etat[1,c]=noir);
constraint etat[1,nbr_m+1]=vide;
constraint forall(c in nbr_m+2..taille_ligne)(etat[1,c]=blanc);
constraint unsolved_step[1]=1;

%On note quand c'est gagné.
constraint forall(s in 2..max_step)(
  (unsolved_step[s]=0 /\ unsolved_step[s-1]=0) \/
  (unsolved_step[s]=0 /\ forall(c in 1..nbr_m)(etat[s,c]=blanc) /\ etat[s,nbr_m+1]=vide /\ forall(c in nbr_m+2..taille_ligne)(etat[s,c]=noir)) \/
  unsolved_step[s]=1
);

%On regarde où saute le mouton s'il est blanc.
constraint forall(s in 1..max_step where unsolved_step[s]=1)(
  etat[s,mouton_sauteur[s]]=blanc -> (
    (etat[s,mouton_sauteur[s]-1]=vide /\ mouton_sauteur[s]-1=case_arrive[s]) \/
    (etat[s,mouton_sauteur[s]-1]!=vide /\ etat[s,mouton_sauteur[s]-2]=vide /\ mouton_sauteur[s]-2=case_arrive[s])
  )
);

%On regarde où saute le mouton s'il est noir.
constraint forall(s in 1..max_step where unsolved_step[s]=1)(
  etat[s,mouton_sauteur[s]]=noir -> (
    (etat[s,mouton_sauteur[s]+1]=vide /\ mouton_sauteur[s]+1=case_arrive[s]) \/
    (etat[s,mouton_sauteur[s]+1]!=vide /\ etat[s,mouton_sauteur[s]+2]=vide /\ mouton_sauteur[s]+2=case_arrive[s])
  )
);

%On verifie que le la case de départ du mouton n'est pas vide
constraint forall(s in 1..max_step where unsolved_step[s]=1)(
  etat[s,mouton_sauteur[s]]!=vide
);

%On bouge le moutons concerné etr seulement lui
constraint forall(s in 1..max_step-1 where unsolved_step[s]=1)(forall(c in 1..taille_ligne)(
  (mouton_sauteur[s]=c -> etat[s+1,mouton_sauteur[s]]=vide) /\
  (case_arrive[s]=c -> etat[s+1,case_arrive[s]]=etat[s,mouton_sauteur[s]]) /\
  ((mouton_sauteur[s]!=c /\ case_arrive[s]!=c) -> etat[s+1,c]=etat[s,c])
));

%On doit avoir fini à la fin
constraint unsolved_step[max_step]=0;

solve minimize sum(unsolved_step)
