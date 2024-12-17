## Lista 02
## Disciplina de Métodos Matriciais
## 
# Criado por Nandara de Bortoli

import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import pandas as pd


# Carregar dado de SLP em .mat
slp_mat = sio.loadmat('slp.mat')

# Carregar dado de SST em .mat
sst_mat = sio.loadmat('sst.mat')


# Pegar matriz SLP no .mat
SLP=slp_mat['SLP']+900
# Calcular media slp
slp_mean=np.nanmean(SLP,axis=0)
# Calcular desvio padrão
slp_stdv=np.nanstd(SLP)

# Pegar matriz SST no .mat
SST=sst_mat['SST']
# Calcular media sst
sst_mean=np.nanmean(SST,axis=0)
# Calcular desvio padrão
sst_stdv=np.nanstd(SST)

# Pegar latitudes e longitudes
LAT= slp_mat['lat']
LON=slp_mat['lon']

# Aplicar reshape para ajustar 
sst = np.reshape(sst_mean,(9,25))
slp = np.reshape(slp_mean,(9,25))
lat = np.reshape(LAT,(9,25))
lon = np.reshape(LON,(9,25))

fig = plt.figure(figsize=(10, 8))
cs = plt.contourf(lon,lat,sst,cmap='coolwarm')
contour = plt.contour(lon,lat,sst, levels = 20,
            colors='k', linewidths=1.0, linestyles='solid')  
contour.clabel(fontsize=10, inline=2, inline_spacing=2, rightside_up=True,
          use_clabeltext=True, fmt='%i')
plt.title('Temperatura superficial do mar')
plt.colorbar(cs,label="ºC", orientation="horizontal")
plt.savefig("SST_grid_plot.png")

fig = plt.figure(figsize=(10, 8))
css = plt.contourf(lon,lat,slp,cmap = 'coolwarm')
contour = plt.contour(lon,lat,slp, levels = 7,
            colors='k', linewidths=1.0, linestyles='solid')  
contour.clabel(fontsize=10, inline=2, inline_spacing=2, rightside_up=True,
          use_clabeltext=True, fmt='%i')
plt.title('Pressão ao nível do mar')
plt.colorbar(css,label = "mb", orientation = "horizontal")
plt.savefig("SLP_grid_plot.png")

#=====================================================================================

    
condicao = (SLP > (slp_mean + 3 * slp_stdv)) | (SLP < (slp_mean - 3 * slp_stdv))
pos1, pos2 = np.where(condicao)
SLP[pos1,pos2] = np.nan
slp_mean  =np.nanmean(SLP,axis = 0)
slp_stdv = np.nanstd(SLP)
slp2 = np.reshape(slp_mean,(9,25))

fig = plt.figure(figsize=(10, 8))  
cax = plt.contourf(lon, lat, slp2, cmap = 'coolwarm')
contour = plt.contour(lon,lat,slp2, levels = 7,
            colors='k', linewidths=1.0, linestyles='solid')  
contour.clabel(fontsize=10, inline=2, inline_spacing=2, rightside_up=True,
        use_clabeltext=True, fmt='%i')
plt.title('Pressão ao nível do mar = Desvio Padrão 1')
cbar = fig.colorbar(cax, orientation = "horizontal", label = "mb")
plt.savefig("SLP_grid_1stdv.png")
  
plt.tight_layout()
plt.show()

# 2 stdv
   
condicao = (SLP > (slp_mean + 3 * slp_stdv)) | (SLP < (slp_mean - 3 * slp_stdv))
pos1, pos2 = np.where(condicao)
SLP[pos1,pos2] = np.nan
slp_mean  =np.nanmean(SLP,axis = 0)
slp_stdv = np.nanstd(SLP)
slp2 = np.reshape(slp_mean,(9,25))

fig = plt.figure(figsize=(10, 8))    
cax = plt.contourf(lon, lat, slp2, cmap = 'coolwarm')
contour = plt.contour(lon,lat,slp2, levels = 7,
            colors='k', linewidths=1.0, linestyles='solid')  
contour.clabel(fontsize=10, inline=2, inline_spacing=2, rightside_up=True,
        use_clabeltext=True, fmt='%i')
plt.title('Pressão ao nível do mar = Desvio Padrão 2')
cbar = fig.colorbar(cax, orientation = "horizontal", label = "mb")
plt.savefig("SLP_grid_2stdv.png")
plt.tight_layout()
plt.show()

# 3 stdv
     
condicao = (SLP > (slp_mean + 3 * slp_stdv)) | (SLP < (slp_mean - 3 * slp_stdv))
pos1, pos2 = np.where(condicao)
SLP[pos1,pos2] = np.nan
slp_mean  =np.nanmean(SLP,axis = 0)
slp_stdv = np.nanstd(SLP)
slp2 = np.reshape(slp_mean,(9,25))

fig = plt.figure(figsize=(10, 8))
cax = plt.contourf(lon, lat, slp2, cmap = 'coolwarm')
contour = plt.contour(lon,lat,slp2, levels = 7,
            colors='k', linewidths=1.0, linestyles='solid')  
contour.clabel(fontsize=10, inline=2, inline_spacing=2, rightside_up=True,
        use_clabeltext=True, fmt='%i')
plt.title('Pressão ao nível do mar = Desvio Padrão 3')
cbar = fig.colorbar(cax, orientation = "horizontal", label = "mb")
plt.savefig("SLP_grid_3stdv.png")
plt.tight_layout()
plt.show()


#=====================================================================================



    
condicao = (SST > (sst_mean + 3 * sst_stdv)) | (SLP < (sst_mean - 3 * sst_stdv))
pos1, pos2 = np.where(condicao)
SST[pos1,pos2] = np.nan
sst_mean  =np.nanmean(SST,axis = 0)
sst_stdv = np.nanstd(SST)
SST2 = np.reshape(sst_mean,(9,25))

fig = plt.figure(figsize=(10, 8))  
cax = plt.contourf(lon, lat, SST2, cmap = 'coolwarm')
contour = plt.contour(lon,lat,SST2, levels = 7,
            colors='k', linewidths=1.0, linestyles='solid')  
contour.clabel(fontsize=10, inline=2, inline_spacing=2, rightside_up=True,
        use_clabeltext=True, fmt='%i')
plt.title( 'Temperatura = Desvio Padrão 1')
cbar = fig.colorbar(cax, orientation = "horizontal", label = "mb")
plt.savefig("SST_grid_1stdv.png")
  
plt.tight_layout()
plt.show()

# 2 stdv
   
condicao = (SST > (sst_mean + 3 * sst_stdv)) | (SST < (sst_mean - 3 * sst_stdv))
pos1, pos2 = np.where(condicao)
SST[pos1,pos2] = np.nan
sst_mean  =np.nanmean(SST,axis = 0)
sst_stdv = np.nanstd(SST)
SST2 = np.reshape(sst_mean,(9,25))

fig = plt.figure(figsize=(10, 8))    
cax = plt.contourf(lon, lat, SST2, cmap = 'coolwarm')
contour = plt.contour(lon,lat,SST2, levels = 7,
            colors='k', linewidths=1.0, linestyles='solid')  
contour.clabel(fontsize=10, inline=2, inline_spacing=2, rightside_up=True,
        use_clabeltext=True, fmt='%i')
plt.title('Temperatura = Desvio Padrão 2')
cbar = fig.colorbar(cax, orientation = "horizontal", label = "mb")
plt.savefig("SST_grid_2stdv.png")
plt.tight_layout()
plt.show()

# 3 stdv
     
condicao = (SST > (sst_mean + 3 * sst_stdv)) | (SST < (sst_mean - 3 * sst_stdv))
pos1, pos2 = np.where(condicao)
SST[pos1,pos2] = np.nan
sst_mean  =np.nanmean(SST,axis = 0)
sst_stdv = np.nanstd(SST)
SST2 = np.reshape(sst_mean,(9,25))

fig = plt.figure(figsize=(10, 8))
cax = plt.contourf(lon, lat, SST2, cmap = 'coolwarm')
contour = plt.contour(lon,lat,SST2, levels = 7,
            colors='k', linewidths=1.0, linestyles='solid')  
contour.clabel(fontsize=10, inline=2, inline_spacing=2, rightside_up=True,
        use_clabeltext=True, fmt='%i')
plt.title('Temperatura = Desvio Padrão 3')
cbar = fig.colorbar(cax, orientation = "horizontal", label = "mb")
plt.savefig("SST_grid_3stdv.png")
plt.tight_layout()
plt.show()

