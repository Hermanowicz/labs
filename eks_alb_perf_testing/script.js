import { sleep } from 'k6'
import http from 'k6/http'

// See https://k6.io/docs/using-k6/options
export const options = {
    insecureSkipTLSVerify: true,
    noConnectionReuse: false,
  stages: [
    { duration: '1m', target: 20 },
    { duration: '3m', target: 50 },
    { duration: '10m', target: 250 },
    { duration: '10m', target: 150 },
    { duration: '1m', target: 35 },
  ],
  thresholds: {
    http_req_failed: ['rate<0.02'], // http errors should be less than 2%
    http_req_duration: ['p(95)<2000'], // 95% requests should be below 2s
  },
}

export default function main() {
  let response = http.get('http://aa8e11e0c067f40d3ace6d81abc30892-835924440.eu-central-1.elb.amazonaws.com/uuid')
  sleep(1)
}