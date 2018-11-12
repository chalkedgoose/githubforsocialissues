import React from 'react'
// import { Link } from 'gatsby'
import Layout from '../components/layout'
import Map from '../components/google_maps'
import Issues from '../components/issues'

class IndexPage extends React.Component {
  
  render() {
    return (
      <Layout className='container'>
        <Map></Map>
        <Issues></Issues>
        <div className='test'>
        hello
        </div>
      </Layout>
    )
  }
} 

export default IndexPage
