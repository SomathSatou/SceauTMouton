include "globals.mzn";

int: nbr_sceau = 3;
array[1..nbr_sceau] of 1..100: taille_sceau = [10,7,2];
int: remplissage_final = 4;
array[1..nbr_sceau] of 0..1: remplissage_initial = [1,0,0];

int: max_step = 6;
enum action = {rien,verser,recevoir};
array[1..max_step] of var 0..1: unsolved_step;
array[1..max_step,1..nbr_sceau] of var 0..10: remplissage;
array[1..max_step,1..nbr_sceau] of var action: actions;
array[1..max_step] of var 1..nbr_sceau: sceau_verseur;
array[1..max_step] of var 1..nbr_sceau: sceau_receveur;

%Tout les sceaux commencent vide ou plein
constraint forall(s in 1..nbr_sceau)(
  remplissage[1,s]=taille_sceau[s]*remplissage_initial[s]
);

%Tout les sceaux doivent finir dans leur état final
constraint unsolved_step[max_step]=0;

%Une fois résolu, on arrète la résolution
constraint forall(s in 1..max_step-1)(
  unsolved_step[s]=0 -> unsolved_step[s+1]=0
);
constraint forall(s in 1..max_step)(
  unsolved_step[s]=0 -> forall(sc in 1..nbr_sceau)(actions[s,sc]=rien)
);

%Tant que c'est pas résolu, on l'indique
constraint forall(s in 1..max_step)(forall(sc in 1..nbr_sceau)(
  remplissage[s,sc]=remplissage_final -> unsolved_step[s]=0
));
constraint forall(s in 1..max_step)(
  unsolved_step[s]=1 <-> forall(sc in 1..nbr_sceau)(remplissage[s,sc]!=remplissage_final)
);

%On fait une seul action par tour
constraint forall(s in 1..max_step)(
  count([actions[s,sc] | sc in 1..nbr_sceau],verser)=1 \/ unsolved_step[s]=0
);
constraint forall(s in 1..max_step)(
  count([actions[s,sc] | sc in 1..nbr_sceau],recevoir)=1 \/ unsolved_step[s]=0
);

%Si on fait rien, il se passe rien
constraint forall(s in 1..max_step-1)(forall(sc in 1..nbr_sceau)(
  actions[s,sc]=rien -> (remplissage[s,sc]=remplissage[s+1,sc])
));

%On retient le sceau verseur et receveur
constraint forall(s in 1..max_step)(forall(sc in 1..nbr_sceau)(
  actions[s,sc]=verser->sceau_verseur[s]=sc
));
constraint forall(s in 1..max_step)(forall(sc in 1..nbr_sceau)(
  actions[s,sc]=recevoir->sceau_receveur[s]=sc
));

%On glisse l'eau
constraint forall(s in 1..max_step-1)(
  remplissage[s+1,sceau_verseur[s]]=remplissage[s,sceau_verseur[s]]-min([remplissage[s,sceau_verseur[s]],(taille_sceau[sceau_receveur[s]]-remplissage[s,sceau_receveur[s]])])
);
constraint forall(s in 1..max_step-1)(
  remplissage[s+1,sceau_receveur[s]]=remplissage[s,sceau_receveur[s]]+min([remplissage[s,sceau_verseur[s]],(taille_sceau[sceau_receveur[s]]-remplissage[s,sceau_receveur[s]])])
);

solve minimize sum(unsolved_step);