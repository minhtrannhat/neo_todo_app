# Neo Todo App Frontend

## Dev Log

### Styling the frontend

- Used the [MUI](mui.com) React component library using Material Design by Google.
- Font used is `Roboto`. Font is imported to `src/App.tsx`.

#### Use ThemeProvider

To override the default MUI looks, we create a ThemeProvider at `src/ThemeProvider.tsx`.

#### React Hook useMemo

useMemo is a React Hook that lets you cache the result of a calculation between re-renders. Made for running expensive synchronous operations less often.

#### MUI (Material UI)

##### Palette Mode

Change default component colors to suit one's needs.

##### CSSBaseline

Reset the CSS injected into `<head>`. A collection of HTML element and attribute style-normalizations, you can expect all of the elements to look the same across all browsers.

##### useMediaQuery

This React hook listens for matches to a CSS media query. It allows the rendering of components based on whether the query matches or not.

##### Container's maxWidth

This will make sure Material UI's Container will not expand to fill the entire screen and instead just stop expanding at around 960px (which is `md`).

### Configure the page's title (Browser Tab Text)

Use `react-helmet-async`, wrap it around the `App` in `App.tsx`.
