<template>
    <div class="tab-pane fade border border-dark " style="height: 75vh" id="v-pills-BuscaProducto" role="tabpanel" aria-labelledby="v-pills-BuscaProducto-tab">
        <div class="tab-pane fade show active " id="v-pills-home" role="tabpanel" aria-labelledby="v-pills-home-tab">     
            <div class="card-header text-center bg-secondary text-white w-100">
                Busca un producto que puedas reutilizar y así contribuir al medio ambiente
            </div>     
        
            <form class="d-flex p-3">
                <div class="input-group mt-3 mx-5">
                    <span class="input-group-text"  style="width: 15em;">Nombre del producto</span>
                    <input type="text" aria-label="First name" class="form-control ">
                    <button class="btn btn-primary ms-3" type="submit">Buscar</button>
                </div>
            </form>
        </div>
        <div class="p-3">      
            <table class="table table-bordered ">
                <thead>
                    <tr class="table-secondary">
                        <th>Producto</th>
                        <th>Estado</th>
                        <th>Direccion</th>
                        <th>Telefono de contacto</th>
                        <th>Imagen</th>
                    </tr>
                </thead>
            
                <tr>
                    <td>Soleado</td>
                    <td>Mayormente soleado</td>
                    <td>Parcialmente nublado</td>
                    <td>Mayormente soleado</td>
                    <td>Parcialmente nublado</td>
                </tr>
                <tr>
                    <td>Soleado</td>
                    <td>Mayormente soleado</td>
                    <td>Parcialmente nublado</td>
                    <td>Mayormente soleado</td>
                    <td>Parcialmente nublado</td>
                </tr>
            </table>
        </div> 
    </div>
</template>