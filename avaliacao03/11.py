Lista Rotina (Lista L, inteiro j) {
	Se (j == 1)
return L;
	Encontre o L[i], o maior item da lista L entre 1 e j;
	Troque o L[i] pelo item L[j];
	return Rotina (L, j – 1);
}
