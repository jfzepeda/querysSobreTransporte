import pandas as pd

MODOS = ['tren','tren_urbano','transporte_electrico','camion_microbus','colectivo',
         'autobus_foraneo','brt','taxi','bicitaxi_mototaxi','transporte_escolar',
         'avion','automovil_particular','tractor','trailer','motocicleta',
         'bicicleta_triciclo','patines_patineta','traccion_animal','animal',
         'helicoptero','embarcacion_mayor','embarcacion_menor']
P1A = {f'p1a_{i+1}': m for i, m in enumerate(MODOS)}

df = pd.read_spss('ENMT.sav', convert_categoricals=False)

# 8 y 9 son NS/NC en esta batería (no 97/98/99)
uso = df[list(P1A)].replace({8: pd.NA, 9: pd.NA}).rename(columns=P1A)

cotidianos = uso.eq(1)
df['n_modos_cotidianos'] = cotidianos.sum(axis=1)
df['modo_principal'] = cotidianos.idxmax(axis=1).where(cotidianos.any(axis=1))
df.loc[df.n_modos_cotidianos > 1, 'modo_principal'] = 'multimodal'
