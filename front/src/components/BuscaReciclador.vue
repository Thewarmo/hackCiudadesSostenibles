<template>
    <div class="tab-pane fade  border border-dark " style="height: 75vh" id="v-pills-BuscaReciclador" role="tabpanel" aria-labelledby="v-pills-BuscaReciclador-tab">
        <div class="card-header text-center bg-secondary text-white w-100">
            Busca un reciclador cerca de tu zona
        </div>  
        <form class="d-flex flex-column p-3 mx-5">
            
            <div class="input-group mt-3">
                <span class="input-group-text" style="width: 15em">
                    Zona
                </span>
                <select class="form-select form-select-sm" aria-label=".form-select-sm example">
                    <option selected>Slecciona tu zona</option>
                    <option value="1">sur</option>
                    <option value="2">norte</option>
                    <option value="3">oriente</option>
                    <option value="3">occidente</option>
                </select>
                
            </div>
            
            <div class="input-group mt-3 border border-1">
                <span class="input-group-text" style="width: 15em">
                    Material
                </span>
                <div class="form-check form-check-inline ms-2 pt-1">
                    <input class="form-check-input" type="checkbox" id="inlineCheckbox1" value="option1">
                    <label class="form-check-label" for="inlineCheckbox1">Vidrio</label>
                </div>
                <div class="form-check form-check-inline pt-1">
                    <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2">
                    <label class="form-check-label" for="inlineCheckbox2">Papel</label>
                </div>
                <div class="form-check form-check-inline pt-1">
                    <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2">
                    <label class="form-check-label" for="inlineCheckbox2">Plastico</label>
                </div>
                <div class="form-check form-check-inline pt-1">
                    <input class="form-check-input" type="checkbox" id="inlineCheckbox2" value="option2">
                    <label class="form-check-label" for="inlineCheckbox2">Aluminio</label>
                </div>
            </div>
            <div class="d-grid gap-2 col-6 mx-auto mt-3">
                <button class="btn btn-primary" type="button">Buscar </button>
            </div>
        </form>
        <div class="p-3">      
            <table class="table table-bordered ">
                <thead>
                    <tr class="table-secondary">
                        <th>Reciclador</th>
                        <th>Zona</th>
                        <th>Material</th>
                        <th>Solicitar</th>
                    </tr>
                </thead>
            
                <tr>
                    <td>Soleado</td>
                    <td>Mayormente soleado</td>
                    <td>Parcialmente nublado</td>
                    <td><button type="button" class="btn btn-secondary btn-sm">Crear Solicitud</button></td>
                </tr>
                <tr>
                    <td>Soleado</td>
                    <td>Mayormente soleado</td>
                    <td>Parcialmente nublado</td>
                    <td><button type="button" class="btn btn-secondary btn-sm">Crear solicitud</button></td>
                </tr>
            </table>
        </div> 
    </div>
</template>