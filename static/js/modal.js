// <!-- Repair Modal -->
var RepairModalCenter = document.getElementById('RepairModalCenter')
RepairModalCenter.addEventListener('show.bs.modal', function (event) {
  // Button that triggered the modal
  var button = event.relatedTarget
  // Extract info from data-bs-* attributes
  var recipient = button.getAttribute('data-bs-whatever')
  // If necessary, you could initiate an AJAX request here
  // and then do the updating in a callback.
  //
  // Update the modal's content.
  var modalTitle = RepairModalCenter.querySelector('.modal-title')
  var modalBodyInput = RepairModalCenter.querySelector('.modal-body input')

  modalTitle.textContent = 'New message to ' + recipient
  modalBodyInput.value = recipient
})

// <!-- Overrule Modal -->
var OverruleModalCenter = document.getElementById('OverruleModalCenter')
OverruleModalCenter.addEventListener('show.bs.modal', function (event) {
  // Button that triggered the modal
  var button = event.relatedTarget
  // Extract info from data-bs-* attributes
  var recipient = button.getAttribute('data-bs-whatever')
  // If necessary, you could initiate an AJAX request here
  // and then do the updating in a callback.
  //
  // Update the modal's content.
  var modalTitle = OverruleModalCenter.querySelector('.modal-title')
  var modalBodyInput = OverruleModalCenter.querySelector('.modal-body input')

  modalTitle.textContent = 'New message to ' + recipient
  modalBodyInput.value = recipient
})

// <!-- Delete Modal -->
var DeleteModalCenter = document.getElementById('DeleteModalCenter')
DeleteModalCenter.addEventListener('show.bs.modal', function (event) {
  // Button that triggered the modal
  var button = event.relatedTarget
  // Extract info from data-bs-* attributes
  var recipient = button.getAttribute('data-bs-whatever')
  // If necessary, you could initiate an AJAX request here
  // and then do the updating in a callback.
  //
  // Update the modal's content.
  var modalTitle = DeleteModalCenter.querySelector('.modal-title')
  var modalBodyInput = DeleteModalCenter.querySelector('.modal-body input')

  modalTitle.textContent = 'New message to ' + recipient
  modalBodyInput.value = recipient
})