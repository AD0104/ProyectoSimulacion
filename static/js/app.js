const dataSection = document.querySelector(".data_section");
const radios = document.querySelector(".data_radios");
let res;
const util = {
  Llegadas: "arrivals",
  Entradas: "entrys",
  Salidas: "outs",
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

      res = await fetchData(form_data);
      console.log(res);

      printData(res.arrivals);
      radios.classList.add("toggleRadios");
    });
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
  printData(res[util[e.target.innerText]]);
};

init();
