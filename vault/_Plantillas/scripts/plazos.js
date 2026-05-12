/**
 * Cálculo de plazos procesales chilenos.
 * Uso en plantilla Templater:
 *   <% tp.user.plazos.diasHabiles(tp.date.now("YYYY-MM-DD"), 5) %>
 *   <% tp.user.plazos.audienciaPreparatoria(tp.date.now("YYYY-MM-DD")) %>
 */

function esDiaHabil(fecha) {
  const dia = fecha.getDay();
  return dia !== 0 && dia !== 6;
}

function sumarDiasHabiles(fechaIso, dias) {
  let fecha = new Date(fechaIso);
  let sumados = 0;
  while (sumados < dias) {
    fecha.setDate(fecha.getDate() + 1);
    if (esDiaHabil(fecha)) sumados++;
  }
  return fecha.toISOString().slice(0, 10);
}

function sumarDiasCorridos(fechaIso, dias) {
  let fecha = new Date(fechaIso);
  fecha.setDate(fecha.getDate() + dias);
  return fecha.toISOString().slice(0, 10);
}

module.exports = {
  diasHabiles: sumarDiasHabiles,
  diasCorridos: sumarDiasCorridos,

  // Plazos procesales penales (Chile)
  apelacion: (fechaIso) => sumarDiasHabiles(fechaIso, 5),
  recursoNulidad: (fechaIso) => sumarDiasHabiles(fechaIso, 10),
  audienciaPreparatoria: (fechaIso) => sumarDiasCorridos(fechaIso, 60),
  cierreInvestigacion: (fechaIso) => sumarDiasCorridos(fechaIso, 730),
  recursoReposicion: (fechaIso) => sumarDiasHabiles(fechaIso, 3),

  // Plazos procesales civiles (Chile)
  contestacionDemanda: (fechaIso) => sumarDiasHabiles(fechaIso, 15),
  apelacionCivil: (fechaIso) => sumarDiasHabiles(fechaIso, 10),
  terminoProbatorio: (fechaIso) => sumarDiasHabiles(fechaIso, 20),
};
