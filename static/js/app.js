const dataSection = document.querySelector(".data_section");
const radios = document.querySelector(".data_radios");

let formatData;
const util = {
  Llegadas: "arrivals",
  Entradas: "entrys",
  Salidas: "outs",
  Promedio: "average",
  Total: "total",
};

const init = () => {
  document.addEventListener("DOMContentLoaded", () => {
    toggleRadio();
    submitEvent();
  });
};

const submitEvent = () => {
  document
    .getElementById("submit-form")
    .addEventListener("click", async (event) => {
      event.preventDefault();
      const form_data = {
        "washing-stations": document.getElementById("washing-stations-entry")
          .value,
        "simulation-time": document.getElementById("simulation-time-entry")
          .value,
        "simulation-day": document.getElementById("sim-day").value,
        workers: document.getElementById("workers").value,
      };

      const res = await fetchData(form_data);
      formatData = convert(res);
      console.log(formatData);

      printData(formatData.arrivals);
      radios.classList.add("toggleRadios");
    });
};

const convert = (res) => {
  return {
    arrivals: res.arrivals,
    entrys: res.entrys,
    outs: res.outs,
    average: [
      `Tiempo promedio de una moto: ${res["bike-average-time"]}`,
      `Tiempo promedio de un carro: ${res["car-average-time"]}`,
      `Tiempo promedio de un trailer: ${res["truck-average-time"]}`,
    ],
    total: [
      `Tiempo total de una moto: ${res["bike-total-time"]}`,
      `Tiempo total de un carro: ${res["car-total-time"]}`,
      `Tiempo total de un trailer: ${res["truck-total-time"]}`,
    ],
  };
};

const fetchData = async (form) => {
  const response = await fetch("/get-form-data", {
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    method: "POST",
    body: JSON.stringify(form),
  });

  return await response.json();
};

const printData = (data) => {
  dataSection.innerHTML = "";
  dataSection.innerHTML = data.map(
    (data) => String.raw`<p class="parrafo">${data}</p>`
  );
};

const toggleRadio = () => {
  document.addEventListener("click", (e) => {
    if (e.target.matches(".label")) {
      document.querySelectorAll(".label").forEach((Element) => {
        Element.matches("checked" && Element.classList.remove("checked"));
      });
      toggleButton(e);
    }
  });
};

const toggleButton = (e) => {
  e.target.classList.toggle("checked");
  printData(formatData[util[e.target.innerText]]);
};

init();
