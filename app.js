'use strict';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { currentColor: 'rgb(255,0,0)' }; // todo find initial value
    this.setColor = this.setColor.bind(this);
  }

  componentDidMount() {
    const { currentColor } = this.state;

    const colorPicker = new iro.ColorPicker("#color-picker", {
      width: 320,
      color: currentColor,
    });

    colorPicker.on('color:change', color => {
      this.setState({ currentColor: color.rgbString });
    });
  }

  setColor() {
    const { currentColor } = this.state;

    // we don't really care about response...
    fetch(`/set-color?color=${this.trimRgbString(currentColor)}`);
  }

  // trims "rgb(255,0,0)" string from color picker to only include the comma delimited numbers (removes "rgb" & the parenthesis)
  trimRgbString(rgb) {
    return rgb.substr(4, rgb.length - 5);
  }

  render() {
    return (
      <div className="container">
        <div>
          <div id="color-picker"></div>

          <div className="button">
            <div className="buttonFace">
              <button className="circle" onClick={this.setColor}></button>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

// Mount the React app.
const domContainer = document.querySelector('#app');
ReactDOM.render(React.createElement(App), domContainer);
